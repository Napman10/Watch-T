from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveUpdateAPIView)

from ...models import Issue
from ...serializers import IssueSerializer
from django.db.models.query import Q
from ....abstract.functional import sanitize_query_params#, request_user
from ...consts import *


class IssueListView(ListAPIView):
    serializer_class = IssueSerializer

    def get_queryset(self):
        params = sanitize_query_params(dict(self.request.query_params))

        somename = params.get('somename')

        author_own = params.get('ownerrel')

        if author_own is not None:
            del params['ownerrel']

        if somename is not None:
            q1 = {**params, "short_name__contains": somename}
            q2 = {**params, "header__contains": somename}
            qs = Issue.objects.filter(Q(**q1) | Q(**q2))
        else:
            qs = Issue.objects.filter(**params)

        #username = request_user.user.username
        username = 'chel'

        if author_own is not None:
            if author_own == ALL:
                return qs
            elif author_own == TO_ME:
                return qs.filter(executor__username=username)
            elif author_own == BY_ME:
                return qs.filter(author__username=username)
            elif author_own == OR:
                return qs.filter(Q(executor__username=username) | Q(author__username=username))
        else:
            return qs


class IssueOpenView(RetrieveUpdateAPIView):
    serializer_class = IssueSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Issue.objects.all()


class IssueCreateView(CreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    action_map = {
        'post': 'create'
    }


class IssueDestroyView(DestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    lookup_field = 'id'
    action_map = {
        'delete': 'delete'
    }
