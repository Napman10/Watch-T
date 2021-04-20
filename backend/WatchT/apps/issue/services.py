import re
from ..abstract.exceptions import NegativeGotTimeException, OverThreeInProgressException, NotAllChildDoneException
from ..project.models import ProjectStatistics
from ..user.models import UserStatistics
from ..abstract.functional import get_user
from django.apps import apps
from datetime import datetime
from django.db.models import Q


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
