from rest_framework import status
from rest_framework.generics import (DestroyAPIView, ListAPIView,
                                     RetrieveUpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ....abstract.functional import sanitize_query_params
from ....abstract.permissions import AssignedStuffOnly, IsCreator
from ...models import Issue
from ...services import (call_recursive_delete, create_issue, edit_issue,
                         filter_issue_list)
from ..serializers.issue import IssueSerializer


class IssueListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = IssueSerializer

    def get_queryset(self):
        return filter_issue_list(self.request)


class IssueOpenView(RetrieveUpdateAPIView):
    serializer_class = IssueSerializer
    permission_classes = (IsAuthenticated, AssignedStuffOnly)
    lookup_field = 'id'

    def get_queryset(self):
        return Issue.objects.all()

    def put(self, request, *args, **kwargs):
        issue = self.get_object()
        return edit_issue(issue, request)


class IssueCreateView(APIView):
    permission_classes = (IsAuthenticated, IsCreator)

    def post(self, request):
        create_issue(request)
        return Response(status=status.HTTP_201_CREATED)


class IssueDestroyView(DestroyAPIView):
    permission_classes = (IsAuthenticated, IsCreator)
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        me = self.get_object()
        call_recursive_delete(me)

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
