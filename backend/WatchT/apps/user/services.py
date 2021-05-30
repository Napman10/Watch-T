from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from ..abstract.exceptions import (IsSeniorNowException,
                                   NonDevGiveSkillException, NotConfirmedPass,
                                   OnlyDevUpLevel, PasswordsDismatchException)
from ..abstract.functional import (email_is_valid, sanitize_query_params,
                                   string_or_empty)
from ..issue.models import IssueType
from ..project.models import Project2User
from ..user.models import EmployeeUser, Skill, UserStatistics


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

    except BaseException:
        raise APIException

    return Response({"username": original_user.username, "detail": "registration successful"},
                    status=status.HTTP_200_OK)


def edit_user(request, user):
    data = request.data

    real_user = user.user

    username = data.get('username')
    if username:
        real_user.username = username
        real_user.save()

    first_name = data.get('first_name')
    if first_name:
        real_user.first_name = first_name
        real_user.save()

    last_name = data.get('last_name')
    if last_name:
        real_user.last_name = last_name
        real_user.save()

    email = data.get('email')
    if email:
        real_user.email = email
        real_user.save()

    role = data.get('role')
    if role:
        user.role = role
        user.save()

    level = data.get('level')
    if level:
        if user.role != EmployeeUser.DEVELOPER:
            raise OnlyDevUpLevel
        if user.level == EmployeeUser.SENIOR:
            raise IsSeniorNowException
        user.level = level
        user.save()

    skill = data.get('skill')
    if skill:
        skill = ['Frontend', 'Backend', 'DevOps', 'Mobile', 'DB', 'SysAdmin'].index(skill)
        if user.role != EmployeeUser.DEVELOPER:
            raise NonDevGiveSkillException
        issue_type = IssueType.objects.get(typo=skill)
        skill = Skill.objects.create(employee=user, skill=issue_type)
        skill.save()

    password = data.get('password')
    confirm = data.get('password2')

    if password != confirm and password:
        raise NotConfirmedPass
    if password:
        real_user.set_password(password)
        real_user.save()


def filter_users(request):
    params = sanitize_query_params(request)
    project_id = params.get('project_id')
    dev = params.get('dev')
    if project_id is not None:
        exclude = params.get('exclude')
        p2u = Project2User.objects.filter(project__id=project_id)
        user_ids = [p.user.id for p in p2u]
        if exclude is not None:
            return EmployeeUser.objects.exclude(id__in=user_ids)
        if dev is not None:
            return EmployeeUser.objects.filter(id__in=user_ids,
                                               role__in=[EmployeeUser.DEVELOPER,
                                                         EmployeeUser.ADMINISTRATOR,
                                                         EmployeeUser.LEAD])
        return EmployeeUser.objects.filter(id__in=user_ids)

    somename = params.get('somename')

    if somename is not None:
        del params['somename']
        q1 = {**params, "user__username__contains": somename}
        q2 = {**params, "user__first_name__contains": somename}
        q3 = {**params, "user__last_name__contains": somename}
        return EmployeeUser.objects.filter(Q(**q1) | Q(**q2) | Q(**q3))
    elif bool(params):
        return EmployeeUser.objects.filter(**params)
    else:
        return EmployeeUser.objects.all()


def assignment_problem(request):
    params = sanitize_query_params(request)

    skill = params['skill']
    priority = params['priority']
    project_id = params['project_id']

    p2u = Project2User.objects.filter(project__id=project_id)
    user_ids_by_projects = [p.user.id for p in p2u]

    skills_ones = Skill.objects.filter(skill__typo=skill)
    skilled_users = [so.employee for so in skills_ones]

    users = EmployeeUser.objects.\
        filter(id__in=user_ids_by_projects, role=EmployeeUser.DEVELOPER, level__gte=priority).order_by('-level')
    for user in users:
        if user in skilled_users:
            return user

    user = EmployeeUser.objects.filter(id__in=user_ids_by_projects, role=EmployeeUser.LEAD).first()
    return user
