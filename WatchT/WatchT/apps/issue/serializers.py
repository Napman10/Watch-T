from rest_framework import serializers

from .models import Comment, Issue, TrackTime
from ..abstract.functional import string_or_empty


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = "__all__"

    author = serializers.SerializerMethodField()
    executor = serializers.SerializerMethodField()
    project = serializers.SerializerMethodField()

    def get_author(self, obj: Issue) -> str:
        return str(obj.author)

    def get_executor(self, obj: Issue) -> str:
        return string_or_empty(obj.executor)

    def get_project(self, obj: Issue) -> str:
        return str(obj.project)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class TrackTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackTime
        fields = '__all__'
