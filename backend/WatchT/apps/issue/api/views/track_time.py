from rest_framework.generics import DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from ....abstract.functional import get_user, sanitize_query_params
from ....abstract.permissions import IsCreator, NonGuest
from ...models import TrackTime
from ...services import (commit_minutes_statistics, create_track, delete_track,
                         track_and_record)
from ..serializers.track_time import TrackDeleteSerializer, TrackTimeSerializer


class TrackCreateView(APIView):
    permission_classes = (IsAuthenticated, NonGuest)

    def post(self, request):
        return create_track(request)


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
    permission_classes = (IsAuthenticated, IsCreator)
    serializer_class = TrackDeleteSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return TrackTime.objects.all()

    def delete(self, request, *args, **kwargs):
        delete_track(self.get_object(), request)
        return super().delete(request, *args, **kwargs)
