from rest_framework import serializers

from ...models import Comment
from ....abstract.functional import month_russian
from datetime import datetime, timedelta


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    author = serializers.SerializerMethodField()
    issue = serializers.SerializerMethodField()
    datetime = serializers.SerializerMethodField()

    def get_datetime(self, obj: Comment) -> str:
        dt = obj.datetime
        now = datetime.now()

        if now.date() - timedelta(1) == dt.date():
            return f"вчера в {dt.hour}:{dt.minute}"
        elif now.date() == dt.date():
            return f"сегодня в {dt.hour}:{dt.minute}"
        elif now.year != dt.year:
            return f"{dt.day} {month_russian(dt.month)} {dt.year} в {dt.hour}:{dt.minute}"
        else:
            return f"{dt.day} {month_russian(dt.month)} в {dt.hour}:{dt.minute}"

    def get_author(self, obj: Comment) -> str:
        return str(obj.author)

    def get_issue(self, obj: Comment) -> str:
        return str(obj.issue)


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text', 'edited',)


class CommentDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id',)
