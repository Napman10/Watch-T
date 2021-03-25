from rest_framework import permissions
from ..project.models import Project2User, Project
from ..issue.models import Issue
from ..user.models import EmployeeUser
from ..abstract.functional import get_user


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


class IsCreator(permissions.BasePermission):
    message = "You do not have permission for this action"

    def has_permission(self, request, view):
        user = get_user(request)
        return user.role in [EmployeeUser.ADMINISTRATOR, EmployeeUser.ANALYST, EmployeeUser.LEAD]


class CanDeleteComment(permissions.BasePermission):
    message = "You can't delete this comment"

    def has_permission(self, request, view):
        comment = view.get_object()
        user = get_user(request)
        return comment.author == user or user.role == EmployeeUser.ADMINISTRATOR


class CanDeleteTrack(permissions.BasePermission):
    message = "You can't delete this track"

    def has_permission(self, request, view):
        track = view.get_object()
        user = get_user(request)
        return track.executor == user or user.role == EmployeeUser.ADMINISTRATOR
