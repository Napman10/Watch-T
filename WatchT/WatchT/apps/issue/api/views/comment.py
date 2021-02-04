from ...serializers import CommentSerializer
from ...models import Comment

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView


class CommentListView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()


class CommentOpenView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Comment.objects.all()


class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    action_map = {
        'post': 'create'
    }
