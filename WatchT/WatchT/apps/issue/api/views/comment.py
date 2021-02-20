from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveAPIView, UpdateAPIView, DestroyAPIView)

from ...models import Comment
from ...serializers import CommentSerializer, CommentUpdateSerializer
from ....abstract.functional import sanitize_query_params


class CommentListView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        params = sanitize_query_params(self.request)
        issue_id = params.get('issue_id')
        if issue_id:
            return Comment.objects.filter(issue__id=issue_id)

        return Comment.objects.none()


class CommentUpdateView(UpdateAPIView):
    serializer_class = CommentUpdateSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Comment.objects.all()


class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    action_map = {
        'post': 'create'
    }


class CommentOpenView(RetrieveAPIView):
    serializer_class = CommentUpdateSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Comment.objects.all()


class CommentDeleteView(DestroyAPIView):
    serializer_class = CommentUpdateSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Comment.objects.all()
