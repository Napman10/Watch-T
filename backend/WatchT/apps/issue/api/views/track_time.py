from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, UpdateAPIView)
from ..serializers.track_time import TrackTimeSerializer, TrackUpdateSerializer, TrackDeleteSerializer
from ...models import TrackTime
from rest_framework.permissions import IsAuthenticated
from ....abstract.functional import sanitize_query_params


class TrackCreateView(CreateAPIView):
    serializer_class = TrackTimeSerializer
    queryset = TrackTime.objects.all()
    permission_classes = (IsAuthenticated,)
    action_map = {
        'post': 'create'
    }


class TrackListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TrackTimeSerializer

    def get_queryset(self):
        params = sanitize_query_params(self.request)
        issue_id = params.get('issue_id')
        if issue_id:
            return TrackTime.objects.filter(issue__id=issue_id)
        return TrackTime.objects.none()


class TrackUpdateView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TrackUpdateSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return TrackTime.objects.all()


class TrackDeleteView(DestroyAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = TrackDeleteSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return TrackTime.objects.all()
