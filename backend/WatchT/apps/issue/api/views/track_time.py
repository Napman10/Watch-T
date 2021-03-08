from rest_framework.generics import (DestroyAPIView,
                                     ListAPIView)
from ..serializers.track_time import TrackTimeSerializer, TrackDeleteSerializer
from ...models import TrackTime
from rest_framework.permissions import IsAuthenticated
from ....abstract.functional import sanitize_query_params
from rest_framework.views import APIView
from ....user.models import EmployeeUser
from ...models import Issue
from rest_framework.response import Response
from rest_framework import status
from ...services import set_got_time


class TrackCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data

        executor = EmployeeUser.objects.filter(user=request.user).first()
        minutes = data.get('minutes')
        text = data.get('text', '')

        if not minutes:
            return Response(data={"detail": "invalid time"}, status=status.HTTP_400_BAD_REQUEST)

        issue_id = data.get('issue_id')
        if issue_id:
            issue = Issue.objects.get(id=issue_id)
            TrackTime.objects.depend_create(issue=issue, minutes=minutes, executor=executor, text=text)
            return Response(status=status.HTTP_201_CREATED)
        return Response(data={"detail": "invalid"}, status=status.HTTP_400_BAD_REQUEST)


class TrackListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TrackTimeSerializer

    def get_queryset(self):
        params = sanitize_query_params(self.request)
        issue_id = params.get('issue_id')
        if issue_id:
            return TrackTime.objects.filter(issue__id=issue_id)
        return TrackTime.objects.none()


class TrackDeleteView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TrackDeleteSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return TrackTime.objects.all()

    def delete(self, request, *args, **kwargs):
        track = self.get_object()
        issue = track.issue
        minutes = -track.minutes
        set_got_time(issue, minutes)

        return super().delete(request, *args, **kwargs)
