from django.db.models.manager import Manager
from ..user.models import EmployeeUser
from ..project.models import Project


class IssueManager(Manager):
    def inherit_from_proj(self, short_name, header, author_username, project_name, want_minutes=1,
                          executor_username=None, description=None):
        author = EmployeeUser.objects.filter(user__username=author_username).first()
        project = Project.objects.filter(short_name=project_name).first()
        query = {"short_name": short_name, "header": header, "author": author,
                 "project": project, "want_minutes": want_minutes, "description": description}
        if executor_username:
            executor = EmployeeUser.objects.filter(user__username=executor_username).first()
            query["executor"] = executor

        self.create(**query)
