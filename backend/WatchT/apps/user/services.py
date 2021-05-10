from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from ..abstract.functional import string_or_empty, email_is_valid
from ..user.models import EmployeeUser, UserStatistics
from ..abstract.exceptions import PasswordsDismatchException
from rest_framework.exceptions import APIException


def user_dict_is_valid(user_data: dict) -> bool:
    username = user_data.get('username')
    first_name = string_or_empty(user_data.get('first_name'))
    last_name = string_or_empty(user_data.get('last_name'))
    email = string_or_empty(user_data.get('email'))

    if len(username) > 150:
        return False

    if len(first_name) > 30:
        return False

    if len(last_name) > 150:
        return False

    if len(email) > 254 or not email_is_valid(email):
        return False

    return True


def create_user(user_data: dict) -> Response:
    password = user_data.get('password')
    password_confirm = user_data.get('password2')

    if bool(password) and password != password_confirm:
        raise PasswordsDismatchException

    del user_data['password2']

    role = user_data.get('role')
    if role:
        if role in [EmployeeUser.ADMINISTRATOR, EmployeeUser.LEAD]:
            level = EmployeeUser.SENIOR
        else:
            level = EmployeeUser.INTERN

        del user_data['role']
    else:
        level = EmployeeUser.INTERN

    try:
        username = user_data.get('username')

        if User.objects.filter(username=username).exists():
            return Response({"detail": f"{username} already exists"}, status=status.HTTP_400_BAD_REQUEST)

        if not user_dict_is_valid(user_data):
            return Response({"detail": "invalid"}, status=status.HTTP_400_BAD_REQUEST)

        original_user = User.objects.create_user(**user_data)
        employee_dict = {"user": original_user}
        if role:
            employee_dict["role"] = role
        if level:
            employee_dict["level"] = level
        user = EmployeeUser.objects.create(**employee_dict)

        UserStatistics.objects.create(user=user)

    except BaseException as e:
        raise APIException

    return Response({"username": original_user.username, "detail": "registration successful"},
                    status=status.HTTP_200_OK)
