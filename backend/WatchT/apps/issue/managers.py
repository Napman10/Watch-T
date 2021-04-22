from django.apps import apps
from django.db.models.manager import Manager

from .services import record_history, track_and_record, can_do_by_qualify, can_do_by_level
from ..abstract.exceptions import BufferWantTimeException
from ..project.models import Project
from ..user.models import EmployeeUser


class IssueManager(Manager):
    def inherit_from_proj(self, short_name, header, author_username, project_name,
                          want_minutes, priority, typo, executor_username=None,
                          description=None, level=1, parent_id=None):
        IssueType = apps.get_model('issue', 'IssueType')

        author = EmployeeUser.objects.filter(user__username=author_username).first()
        project = Project.objects.filter(short_name=project_name).first()
        typo = IssueType.objects.filter(typo=typo).first()

        query = {"short_name": short_name, "header": header, "author": author,
                 "project": project, "got_minutes": 0, "priority": priority,
                 "level": level, "typo": typo}

        if executor_username:
            executor = EmployeeUser.objects.filter(user__username=executor_username).first()
            if executor:
                can_do_by_qualify(typo.typo, executor)
                can_do_by_level(priority, executor)
                query["executor"] = executor

        if want_minutes:
            if parent_id:
                parent = self.get(id=parent_id)
                buffer = parent.want_buffer_minutes
                if buffer - want_minutes >= 0:
                    parent.want_buffer_minutes -= want_minutes
                    parent.save()
                    query['parent'] = parent
                else:
                    raise BufferWantTimeException

            query['want_minutes'] = want_minutes
            query['want_buffer_minutes'] = want_minutes

        if description:
            query['description'] = description

        issue = self.create(**query)
        record_history(issue=issue, text="Задача была создана")


class TrackTimeManager(Manager):
    def depend_create(self, me, issue, minutes, executor, text):
        track_and_record(me, issue, minutes)
        self.create(issue=issue, minutes=minutes, executor=executor, text=text)
