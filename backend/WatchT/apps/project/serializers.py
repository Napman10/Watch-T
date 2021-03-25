from rest_framework import serializers

from .models import Project, ProjectStatistics

from ..abstract.functional import convert_last_seen


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStatistics
        fields = ('created_date', 'tracked_minutes')

    created_date = serializers.SerializerMethodField()

    def get_created_date(self, obj: ProjectStatistics) -> str:
        return convert_last_seen(obj.created_date)
