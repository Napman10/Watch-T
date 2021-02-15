from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveUpdateAPIView)

from ...models import Issue
from ...serializers import IssueSerializer
from django.db.models.query import Q
from ....abstract.functional import sanitize_query_params
from ...consts import *
from rest_framework.permissions import IsAuthenticated


class IssueListView(ListAPIView):
    serializer_class = IssueSerializer
    permission_classes = (IsAuthenticated,)

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


class IssueCreateView(CreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = (IsAuthenticated,)
    action_map = {
        'post': 'create'
    }


class IssueDestroyView(DestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'
    action_map = {
        'delete': 'delete'
    }
