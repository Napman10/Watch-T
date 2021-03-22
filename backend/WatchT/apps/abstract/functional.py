import re
from ..user.models import EmployeeUser


def sanitize_query_params(request):
    query_params = request.query_params
    dictionary = dict(query_params)
    return {k: v[0] for k, v in dictionary.items() if v[0]}


def string_or_empty(val):
    return str(val) if val is not None else ""


def email_is_valid(email: str) -> bool:
    regex = re.compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
    if regex.match(email):
        return True

    return False


def month_russian(month):
    month = int(month) - 1
    months = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
    return months[month]


def get_user(request):
    pure_user = request.user
    return EmployeeUser.objects.filter(user=pure_user).first()


def get_user_dict(user):
    pure = user.user
    return {'id': user.id, 'photo': user.photo, 'role': user.role,
            'first_name': pure.first_name, 'last_name': pure.last_name,
            'email': pure.email, 'username': pure.username}
