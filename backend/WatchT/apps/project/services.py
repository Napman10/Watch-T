from .models import Project, Project2User

from ..abstract.functional import sanitize_query_params, get_user
from django.db.models.query import Q
from rest_framework.exceptions import APIException
from ..user.models import EmployeeUser
from ..issue.models import Issue


def filter_projects(request):
    qs = Project.objects.all()
    data = sanitize_query_params(request)
    somename = data.get('somename')
    assigned = data.get('assigned') == "true"

    if somename is not None:
        qs = qs.filter(Q(short_name__contains=somename) | Q(header__contains=somename))

    if assigned:
        me = get_user(request)
        p2u = Project2User.objects.filter(user=me)
        p2u_ids = [p.project.id for p in p2u]
        qs = qs.filter(id__in=p2u_ids)

    return qs


def edit_project(request, project):
    data = request.data

    short_name = data.get('short_name')
    header = data.get('header')
    description = data.get('description')

    if short_name:
        project.short_name = short_name
    if header:
        project.header = header
    if description:
        project.description = description
    project.save()


def initialize_user_project_pair(request):
    data = request.data
    if not data:
        data = sanitize_query_params(request)
    username = data.get('user')
    if not username:
        raise APIException
    project_id = data.get('project_id')
    if not project_id:
        raise APIException
    user = EmployeeUser.objects.filter(user__username=username).first()
    project = Project.objects.get(id=project_id)
    return user, project


def delete_p2u(request):
    user, project = initialize_user_project_pair(request)
    p = Project2User.objects.filter(user=user, project=project).first()
    if p:
        project = p.project
        issues = Issue.objects.filter(project=project)
        for issue in issues:
            issue.executor = None
            issue.save()
        p.delete()
