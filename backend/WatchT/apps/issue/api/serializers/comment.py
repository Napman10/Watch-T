from rest_framework import serializers

from ....abstract.functional import convert_last_seen
from ...models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    author = serializers.SerializerMethodField()
    issue = serializers.SerializerMethodField()
    datetime = serializers.SerializerMethodField()

    def get_datetime(self, obj: Comment) -> str:
        return convert_last_seen(obj.datetime)

    def get_author(self, obj: Comment) -> str:
        return str(obj.author)

    def get_issue(self, obj: Comment) -> str:
        return str(obj.issue)


class CommentDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id',)
