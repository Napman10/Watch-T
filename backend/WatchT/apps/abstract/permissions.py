from rest_framework import permissions
from ..project.models import Project2User, Project
from ..issue.models import Issue
from ..user.models import EmployeeUser


class AssignedStuffOnly(permissions.BasePermission):
    message = "You do not have permission to watch this project"

    def has_permission(self, request, view):
        pure_user = request.user
        user = EmployeeUser.objects.filter(user=pure_user).first()
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
