from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveAPIView, UpdateAPIView, DestroyAPIView)

from ...models import Comment, Issue
from rest_framework.permissions import IsAuthenticated
from ..serializers.comment import CommentSerializer, CommentUpdateSerializer
from rest_framework.views import APIView
from ....abstract.functional import sanitize_query_params
from ....user.models import EmployeeUser
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status


class CommentListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        params = sanitize_query_params(self.request)
        issue_id = params.get('issue_id')
        if issue_id:
            return Comment.objects.filter(issue__id=issue_id)

        return Comment.objects.none()


class CommentUpdateView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentUpdateSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Comment.objects.all()

    def put(self, request, *args, **kwargs):
        self.request.data['edited'] = True
        return super().put(self.request, *args, **kwargs)


class CommentCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        text = data.get('text')
        issue_id = data.get('issue_id')

        issue = Issue.objects.get(id=issue_id)

        author = EmployeeUser.objects.filter(user=request.user).first()
        dt = datetime.now()
        Comment.objects.create(text=text, issue=issue, author=author, datetime=dt)
        return Response(status=status.HTTP_201_CREATED)


class CommentOpenView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Comment.objects.all()


class CommentDeleteView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentUpdateSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Comment.objects.all()
