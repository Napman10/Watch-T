from rest_framework.generics import (DestroyAPIView,
                                     ListAPIView, RetrieveUpdateAPIView)
from ...models import Issue
from ..serializers.issue import IssueSerializer
from django.db.models.query import Q
from ....abstract.functional import sanitize_query_params
from ...consts import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...services import set_got_time
from ....user.models import EmployeeUser
from ....project.models import Project2User
from rest_framework.exceptions import APIException


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
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return Issue.objects.all()

    def put(self, request, *args, **kwargs):
        issue = self.get_object()
        executor_username = request.data.get('user')
        employee = EmployeeUser.objects.filter(user__username=executor_username).first()
        p2u = Project2User.objects.filter(user=employee, project=issue.project).exists()
        if p2u:
            issue.executor = employee
            issue.save()
            return Response(status=status.HTTP_200_OK)
        raise APIException


class IssueCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data

        short_name = data.get('short_name')
        header = data.get('header')
        author_username = request.user.username
        project_name = data.get('project_name')
        executor_username = data.get('executor_username')

        want_minutes = data.get('want_time')

        priority = data.get('priority')

        description = data.get('description')

        parent_id = data.get('parent')

        level = data.get('level')
        if not level:
            level = 1

        Issue.objects.inherit_from_proj(short_name=short_name, header=header, author_username=author_username,
                                        project_name=project_name, want_minutes=want_minutes,
                                        priority=priority, executor_username=executor_username,
                                        description=description, level=level,
                                        parent_id=parent_id)
        return Response(status=status.HTTP_201_CREATED)


class IssueDestroyView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
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
