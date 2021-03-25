from rest_framework import serializers

from ...models import IssueHistoryRecord
from ....abstract.functional import convert_last_seen


class IssueHistoryRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueHistoryRecord
        fields = '__all__'

    issue = serializers.SerializerMethodField()
    datetime = serializers.SerializerMethodField()

    def get_datetime(self, obj: IssueHistoryRecord) -> str:
        return convert_last_seen(obj.datetime)

    def get_issue(self, obj: IssueHistoryRecord) -> str:
        return str(obj.issue)
