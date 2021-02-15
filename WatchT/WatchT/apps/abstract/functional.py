import re


def sanitize_query_params(dictionary: dict):
    return {k: v[0] for k, v in dictionary.items() if v[0]}


def string_or_empty(val):
    return str(val) if val is not None else ""


def email_is_valid(email: str) -> bool:
    regex = re.compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
    if regex.match(email):
        return True

    return False
