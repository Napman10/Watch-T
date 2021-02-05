from rest_framework import serializers

from .models import Comment, Issue, TrackTime


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('id', 'short_name', 'header', 'description', 'project', 'author', 'executor',
                  'priority', 'status', 'want_minutes', 'got_minutes', 'parent', 'level')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'datetime', 'edited', 'issue')


class TrackTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackTime
        fields = ('id', 'minutes', 'executor', 'issue')
