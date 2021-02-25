from rest_framework import serializers

from ...models import TrackTime


class TrackTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackTime
        fields = '__all__'

    executor = serializers.SerializerMethodField()

    def get_executor(self, obj: TrackTime) -> str:
        return str(obj.executor)


class TrackUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackTime
        fields = ('id', 'time',)


class TrackDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackTime
        fields = ('id',)
