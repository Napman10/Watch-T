import re


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

        return minutes + hours * 60 + days * 24 * 60 + weeks * 7 * 24 * 60

    return None
