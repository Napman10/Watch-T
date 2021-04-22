from rest_framework.generics import (DestroyAPIView,
                                     ListAPIView, RetrieveUpdateAPIView)
from ...models import Issue
from ..serializers.issue import IssueSerializer
from django.db.models.query import Q
from ....abstract.functional import sanitize_query_params, get_user, string_or_empty
from ...consts import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...services import set_got_time, record_history, over_three_check_stat, over_three_check_employee, \
    all_child_done_check, can_do_by_qualify, can_do_by_level
from ....user.models import EmployeeUser
from rest_framework.exceptions import APIException
from ....abstract.permissions import AssignedStuffOnly, IsCreator
from ....project.models import Project2User


class IssueListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = IssueSerializer

    def get_queryset(self):
        params = sanitize_query_params(self.request)

        somename = params.get('somename')

        author_own = params.get('ownerrel')

        if author_own is not None:
            del params['ownerrel']

        if somename is not None:
            del params['somename']
            q1 = {**params, "short_name__contains": somename}
            q2 = {**params, "header__contains": somename}
            qs = Issue.objects.filter(Q(**q1) | Q(**q2))
        else:
            qs = Issue.objects.filter(**params)

        qs = qs.order_by('-priority', '-created')
        username = self.request.user.username

        if author_own is not None:
            if author_own == ALL:
                return qs
            elif author_own == TO_ME:
                return qs.filter(executor__user__username=username)
            elif author_own == BY_ME:
                return qs.filter(author__user__username=username)
            elif author_own == OR:
                return qs.filter(Q(executor__user__username=username) | Q(author__user__username=username))
        else:
            return qs


class IssueOpenView(RetrieveUpdateAPIView):
    serializer_class = IssueSerializer
    permission_classes = (IsAuthenticated, AssignedStuffOnly)
    lookup_field = 'id'

    def get_queryset(self):
        return Issue.objects.all()

    def put(self, request, *args, **kwargs):
        issue = self.get_object()
        me = get_user(request)
        executor_username = request.data.get('user')
        unassign = "Не назначено"
        if executor_username == unassign:
            employee = None
        else:
            employee = EmployeeUser.objects.filter(user__username=executor_username).first()
            over_three_check_employee(issue, employee)
        stat = request.data.get('status')
        good_roles = [EmployeeUser.ADMINISTRATOR, EmployeeUser.LEAD, EmployeeUser.DEVELOPER]
        if executor_username and ((employee and employee.role in good_roles) or not employee):
            can_do_by_qualify(issue.typo.typo, employee)
            can_do_by_level(issue.priority, employee)
            old_executor = issue.executor
            issue.executor = employee
            issue.save()
            record_history(issue=issue,
                           text=f"{me}: исполнитель {string_or_empty(old_executor)} -> {string_or_empty(employee)}")
            return Response(status=status.HTTP_200_OK)

        good_role = me.role in good_roles
        is_my_task = issue.executor == me
        cond = good_role or is_my_task
        if stat and cond:
            over_three_check_stat(issue, stat)
            all_child_done_check(issue, stat)
            old_status = issue.status
            issue.status = stat
            issue.save()
            s = Issue.STATUS_CHOICES
            record_history(issue=issue, text=f"{me}: статус {s[old_status][1]} -> {s[stat][1]}")
            return Response(status=status.HTTP_200_OK)

        raise APIException


class IssueCreateView(APIView):
    permission_classes = (IsAuthenticated, IsCreator)

    def post(self, request):
        data = request.data

        short_name = data.get('short_name')
        header = data.get('header')
        author_username = request.user.username
        project_name = data.get('project_name')
        executor_username = data.get('executor_username')
        typo = data.get('typo')

        want_minutes = data.get('want_time')

        priority = data.get('priority')

        description = data.get('description')

        parent_id = data.get('parent')

        level = data.get('level')
        if not level:
            level = 1

        if not (Project2User.objects.filter(user__user__username=author_username).exists()
                or get_user(request).role == EmployeeUser.ADMINISTRATOR):
            raise APIException

        Issue.objects.inherit_from_proj(short_name=short_name, header=header, author_username=author_username,
                                        project_name=project_name, want_minutes=want_minutes,
                                        priority=priority, executor_username=executor_username,
                                        description=description, level=level,
                                        parent_id=parent_id, typo=typo)
        return Response(status=status.HTTP_201_CREATED)


class IssueDestroyView(DestroyAPIView):
    permission_classes = (IsAuthenticated, IsCreator)
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        me = self.get_object()
        parent = me.parent
        if parent:
            parent.want_buffer_minutes += me.want_minutes
            parent.save()

        minutes = -me.got_minutes
        set_got_time(me, minutes)

        return super().delete(request, *args, **kwargs)


class IssueChildListView(ListAPIView):
    serializer_class = IssueSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        params = sanitize_query_params(self.request)
        parent_id = params.get('id')

        if parent_id:
            parent = Issue.objects.get(id=parent_id)
            return Issue.objects.filter(parent=parent)

        return Issue.objects.none()
