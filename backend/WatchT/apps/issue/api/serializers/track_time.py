from rest_framework import serializers

from ...models import TrackTime


class TrackTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackTime
        fields = '__all__'
