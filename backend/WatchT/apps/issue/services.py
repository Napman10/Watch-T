import re
from ..abstract.exceptions import NegativeGotTimeException
from ..project.models import ProjectStatistics
from ..user.models import UserStatistics
from ..abstract.functional import get_user


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
