from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from ....abstract.functional import sanitize_query_params
from ...models import IssueHistoryRecord
from ..serializers.history import IssueHistoryRecordSerializer


class IssueHistoryRecordListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = IssueHistoryRecordSerializer

    def get_queryset(self):
        params = sanitize_query_params(self.request)
        issue_id = params.get('issue_id')
        if issue_id:
            return IssueHistoryRecord.objects.filter(issue__id=issue_id).order_by('datetime')

        return IssueHistoryRecord.objects.none()
