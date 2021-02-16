from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('short_name',)
