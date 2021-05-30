import re
from datetime import date, datetime

from django.apps import apps
from django.db.models import Q, Sum
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from ..abstract.exceptions import (DoesNotHaveQualificationException,
                                   ImportantThanParentException,
                                   NegativeGotTimeException,
                                   NotAllChildDoneException,
                                   OverThreeInProgressException,
                                   OverTimeException, VeryYoungException)
from ..abstract.functional import (get_user, sanitize_query_params,
                                   string_or_empty)
from ..project.models import Project2User, ProjectStatistics
from ..user.models import EmployeeUser, Skill, UserStatistics
from .consts import *


def call_recursive_delete(issue):
    parent = issue.parent
    if parent:
        parent.want_buffer_minutes += issue.want_minutes
        parent.save()

    minutes = -issue.got_minutes
    set_got_time(issue, minutes)


def create_issue(request):
    Issue = apps.get_model('issue', 'Issue')

    data = request.data

    short_name = data.get('short_name')
    header = data.get('header')
    author_username = request.user.username
    project_name = data.get('project_name')
    executor_username = data.get('executor_username')
    typo = data.get('typo')

    want_minutes = data.get('want_time')

    priority = data.get('priority')

    description = data.get('description')

    parent_id = data.get('parent')

    level = data.get('level')
    if not level:
        level = 1

    if not (Project2User.objects.filter(user__user__username=author_username).exists()
            or get_user(request).role == EmployeeUser.ADMINISTRATOR):
        raise APIException

    Issue.objects.inherit_from_proj(short_name=short_name, header=header, author_username=author_username,
                                    project_name=project_name, want_minutes=want_minutes,
                                    priority=priority, executor_username=executor_username,
                                    description=description, level=level,
                                    parent_id=parent_id, typo=typo)


def filter_issue_list(request):
    Issue = apps.get_model('issue', 'Issue')

    params = sanitize_query_params(request)

    somename = params.get('somename')

    author_own = params.get('ownerrel')

    if author_own is not None:
        del params['ownerrel']

    if somename is not None:
        del params['somename']
        q1 = {**params, "short_name__contains": somename}
        q2 = {**params, "header__contains": somename}
        qs = Issue.objects.filter(Q(**q1) | Q(**q2))
    else:
        qs = Issue.objects.filter(**params)

    qs = qs.order_by('-priority', '-created')
    username = request.user.username

    if author_own is not None:
        if author_own == ALL:
            return qs
        elif author_own == TO_ME:
            return qs.filter(executor__user__username=username)
        elif author_own == BY_ME:
            return qs.filter(author__user__username=username)
        elif author_own == OR:
            return qs.filter(Q(executor__user__username=username) | Q(author__user__username=username))
    else:
        return qs


def edit_issue(issue, request):
    Issue = apps.get_model('issue', 'Issue')

    me = get_user(request)
    executor_username = request.data.get('user')
    unassign = "Не назначено"
    if executor_username == unassign:
        employee = None
    else:
        employee = EmployeeUser.objects.filter(user__username=executor_username).first()
        over_three_check_employee(issue, employee)
    stat = request.data.get('status')
    good_roles = [EmployeeUser.ADMINISTRATOR, EmployeeUser.LEAD, EmployeeUser.DEVELOPER]
    if executor_username and ((employee and employee.role in good_roles) or not employee):
        if employee:
            can_do_by_qualify(issue.typo.typo, employee)
            can_do_by_level(issue.priority, employee)
        old_executor = issue.executor
        issue.executor = employee
        issue.save()
        record_history(issue=issue,
                       text=f"{me}: исполнитель {string_or_empty(old_executor)} -> {string_or_empty(employee)}")
        return Response(status=status.HTTP_200_OK)

    good_role = me.role in good_roles
    is_my_task = issue.executor == me
    cond = good_role or is_my_task
    if stat and cond:
        over_three_check_stat(issue, stat)
        all_child_done_check(issue, stat)
        old_status = issue.status
        issue.status = stat
        issue.save()
        s = Issue.STATUS_CHOICES
        record_history(issue=issue, text=f"{me}: статус {s[old_status][1]} -> {s[stat][1]}")
        return Response(status=status.HTTP_200_OK)

    raise APIException


def is_high_role(employee):
    return employee.role in [EmployeeUser.LEAD, EmployeeUser.ADMINISTRATOR]


def can_do_by_qualify(typo, employee):
    if not Skill.objects.filter(skill__typo=typo, employee=employee).exists() and not is_high_role(employee):
        raise DoesNotHaveQualificationException


def can_do_by_level(priority, employee):
    if priority > employee.level and not is_high_role(employee):
        raise VeryYoungException


def tasks_in_progress(employee):
    Issue = apps.get_model('issue', 'Issue')

    return Issue.objects \
        .filter(executor=employee,
                status__in=[Issue.IN_PROGRESS, Issue.CHECK]) \
        .count()


def over_three_check(employee):
    MAX_IN_PROGRESS = 3
    if tasks_in_progress(employee) == MAX_IN_PROGRESS:
        raise OverThreeInProgressException


def over_three_check_stat(issue, new_status):
    Issue = apps.get_model('issue', 'Issue')

    employee = issue.executor
    old_status = issue.status

    is_progress_check_proc = new_status == Issue.IN_PROGRESS \
                             and old_status == Issue.CHECK \
                             or old_status == Issue.IN_PROGRESS \
                             and new_status == Issue.CHECK

    if not is_progress_check_proc and new_status in [Issue.IN_PROGRESS, Issue.CHECK]:
        over_three_check(employee)


def over_three_check_employee(issue, new_employee):
    Issue = apps.get_model('issue', 'Issue')

    if issue.status in [Issue.IN_PROGRESS, Issue.CHECK]:
        over_three_check(new_employee)


def all_child_done_check(issue, stat):
    Issue = apps.get_model('issue', 'Issue')

    next_stat_done = stat == Issue.DONE
    if next_stat_done:
        got_not_completed_child = Issue.objects.filter(Q(parent=issue) & ~Q(status=Issue.DONE)).exists()
        if got_not_completed_child:
            raise NotAllChildDoneException


def get_period_size(lst):
    return int(lst[0][0]) if len(lst) != 0 else 0


def string_to_issue_time(string):
    format_re = re.compile('^\s*\d*н?\s*\d*д?\s*\d*ч?\s*\d*м?\s*$')
    if format_re.match(string):
        week_re = re.compile('\d+н')
        day_re = re.compile('\d+д')
        hour_re = re.compile('\d+ч')
        minute_re = re.compile('\d+м')

        weeks = get_period_size(week_re.findall(string))
        days = get_period_size(day_re.findall(string))
        hours = get_period_size(hour_re.findall(string))
        minutes = get_period_size(minute_re.findall(string))

        return minutes + hours * 60 + days * 480 + weeks * 2400

    return None


def minutes_to_string(minutes):
    result = ""
    weeks = minutes // (60 * 8 * 5)
    if weeks > 0:
        minutes -= weeks * (60 * 8 * 5)
        result += f"{weeks}н "
    days = minutes // (60 * 8)
    if days > 0:
        minutes -= days * (60 * 8)
        result += f"{days}д "
    hours = minutes // 60
    if hours > 0:
        minutes -= hours * 60
        result += f"{hours}ч "
    if minutes > 0:
        result += f"{minutes}м "
    return result


def set_got_time(issue, minutes):
    issue.got_minutes += minutes
    if issue.got_minutes < 0:
        raise NegativeGotTimeException
    issue.save()
    if issue.parent:
        set_got_time(issue.parent, minutes)


def commit_minutes_statistics(request, issue, minutes):
    project_stat = ProjectStatistics.objects.filter(project=issue.project).first()
    project_stat.tracked_minutes += minutes
    project_stat.save()
    user = get_user(request)
    user_stat = UserStatistics.objects.filter(user=user).first()
    user_stat.tracked_minutes += minutes
    user_stat.save()


def record_history(issue, text):
    IssueHistoryRecord = apps.get_model("issue", "IssueHistoryRecord")
    IssueHistoryRecord.objects.create(issue=issue, text=text, datetime=datetime.now())


def track_and_record(me, issue, minutes):
    got = issue.got_minutes
    text_history = f"{me}: время {minutes_to_string(got)}->{minutes_to_string(got + minutes)}"
    set_got_time(issue, minutes)
    record_history(issue, text_history)


def check_parent_priority(priority, parent_id):
    Issue = apps.get_model('issue', 'Issue')
    parent = Issue.objects.get(id=parent_id)
    if priority > parent.priority:
        raise ImportantThanParentException


def create_track(request):
    Issue = apps.get_model('issue', 'Issue')
    TrackTime = apps.get_model('issue', 'TrackTime')

    data = request.data
    me = get_user(request)
    executor = EmployeeUser.objects.filter(user=request.user).first()
    minutes = data.get('minutes')
    text = data.get('text', '')

    if not minutes:
        raise APIException

    full_day = 60 * 8
    all_tracks_today = TrackTime.objects.filter(executor=executor, datetime__date=date.today()) \
        .aggregate(Sum('minutes'))
    all_tracks_today = all_tracks_today.get('minutes__sum', 0) or 0

    if full_day - all_tracks_today - minutes < 0:
        raise OverTimeException

    issue_id = data.get('issue_id')
    if issue_id:
        issue = Issue.objects.get(id=issue_id)
        TrackTime.objects.depend_create(me=me, issue=issue, minutes=minutes, executor=executor, text=text)
        commit_minutes_statistics(request, issue, minutes)
        return Response(status=status.HTTP_201_CREATED)
    raise APIException


def delete_track(track, request):
    me = get_user(request)
    issue = track.issue
    minutes = -track.minutes
    track_and_record(me, issue, minutes)
    commit_minutes_statistics(request, issue, minutes)
