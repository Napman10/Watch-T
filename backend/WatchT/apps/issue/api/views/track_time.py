from rest_framework.generics import (DestroyAPIView,
                                     ListAPIView)
from ..serializers.track_time import TrackTimeSerializer, TrackDeleteSerializer
from ...models import TrackTime
from rest_framework.permissions import IsAuthenticated
from ....abstract.functional import sanitize_query_params, get_user
from rest_framework.views import APIView
from ...services import commit_minutes_statistics, track_and_record, create_track, delete_track
from ....abstract.permissions import IsCreator, NonGuest


class TrackCreateView(APIView):
    permission_classes = (IsAuthenticated, NonGuest)

    def post(self, request):
        create_track(request)


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
