from rest_framework import serializers

from ...models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    author = serializers.SerializerMethodField()
    issue = serializers.SerializerMethodField()

    def get_author(self, obj: Comment) -> str:
        return str(obj.author)

    def get_issue(self, obj: Comment) -> str:
        return str(obj.issue)


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text', 'edited', )


class CommentDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id',)
