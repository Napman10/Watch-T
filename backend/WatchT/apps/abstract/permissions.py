from rest_framework import permissions

from ..abstract.functional import get_user
from ..issue.models import Issue
from ..project.models import Project, Project2User
from ..user.models import EmployeeUser


class AssignedStuffOnly(permissions.BasePermission):
    message = "You do not have permission to watch this project"

    def has_permission(self, request, view):
        user = get_user(request)
        if user.role == EmployeeUser.ADMINISTRATOR:
            return True

        obj = view.get_object()
        if isinstance(obj, Issue):
            project = obj.project
        elif isinstance(obj, Project):
            project = obj
        else:
            print("permission error")
            raise BaseException

        return Project2User.objects.filter(user=user, project=project).exists()


class IsAdmin(permissions.BasePermission):
    message = "You must be an admin"

    def has_permission(self, request, view):
        user = get_user(request)
        return user.role == EmployeeUser.ADMINISTRATOR


class AdminEditProject(permissions.BasePermission):
    message = "You must be an admin"

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        user = get_user(request)
        return user.role == EmployeeUser.ADMINISTRATOR


class IsCreator(permissions.BasePermission):
    message = "You do not have permission for this action"

    def has_permission(self, request, view):
        user = get_user(request)
        return user.role in [EmployeeUser.ADMINISTRATOR, EmployeeUser.MANAGER, EmployeeUser.LEAD]


class NonAdminChange(permissions.BasePermission):
    message = "You do not have permission for edit/delete an admin user"

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True

        user = get_user(request)
        c_user = view.get_object()

        return user == c_user or c_user.role != EmployeeUser.ADMINISTRATOR


class NonGuest(permissions.BasePermission):
    message = "You are a guest"

    def has_permission(self, request, view):
        user = get_user(request)
        return user.role != EmployeeUser.GUEST
