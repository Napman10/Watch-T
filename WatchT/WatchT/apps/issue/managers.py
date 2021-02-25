from django.db.models.manager import Manager
from ..user.models import EmployeeUser
from ..project.models import Project


class IssueManager(Manager):
    def inherit_from_proj(self, short_name, header, author_username, project_name, want_minutes, priority,
                          executor_username=None, description=None, level=1, parent_id=None):
        author = EmployeeUser.objects.filter(user__username=author_username).first()
        project = Project.objects.filter(short_name=project_name).first()
        query = {"short_name": short_name, "header": header, "author": author,
                 "project": project, "got_minutes": 0, "priority": priority, "level": level}
        if executor_username:
            executor = EmployeeUser.objects.filter(user__username=executor_username).first()
            query["executor"] = executor

        if want_minutes:
            query['want_minutes'] = want_minutes

        if description:
            query['description'] = description

        if parent_id:
            parent = self.get(id=parent_id)
            query['parent'] = parent

        self.create(**query)
