from ...models import Issue
from ...serializers import IssueSerializer

from rest_framework.generics import DestroyAPIView, ListAPIView, RetrieveUpdateAPIView, CreateAPIView


class IssueListView(ListAPIView):
    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.all()


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
