from rest_framework import serializers

from .models import Comment, Issue, TrackTime


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class TrackTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackTime
        fields = '__all__'
