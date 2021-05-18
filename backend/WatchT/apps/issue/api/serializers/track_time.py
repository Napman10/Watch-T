from rest_framework import serializers

from ....abstract.functional import convert_last_seen
from ...models import TrackTime


class TrackTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackTime
        fields = '__all__'

    executor = serializers.SerializerMethodField()
    datetime = serializers.SerializerMethodField()

    def get_executor(self, obj: TrackTime) -> str:
        return str(obj.executor)

    def get_datetime(self, obj: TrackTime) -> str:
        return convert_last_seen(obj.datetime)


class TrackDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackTime
        fields = ('id',)
