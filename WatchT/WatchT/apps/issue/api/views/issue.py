from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveUpdateAPIView)
from rest_framework.response import Response
from rest_framework import status
from ...models import Issue
from ...serializers import IssueSerializer
from django.db.models.query import Q
from ....abstract.functional import sanitize_query_params
from ...consts import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from ...services import string_to_issue_time


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


class IssueCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data

        short_name = data.get('short_name')
        header = data.get('header')
        author_username = request.user.username
        project_name = data.get('project_name')

        want_time_str = data.get('want_time')
        want_minutes = string_to_issue_time(want_time_str)

        priority = data.get('priority')
        executor_username = data.get('executor_username')
        description = data.get('description')

        try:
            Issue.objects.inherit_from_proj(short_name=short_name, header=header, author_username=author_username,
                                            project_name=project_name, want_minutes=want_minutes, priority=priority,
                                            executor_username=executor_username, description=description)
            return Response(status=status.HTTP_201_CREATED)
        except BaseException:
            return Response(data={"detail": "invalid"}, status=status.HTTP_400_BAD_REQUEST)


class IssueDestroyView(DestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'
    action_map = {
        'delete': 'delete'
    }
