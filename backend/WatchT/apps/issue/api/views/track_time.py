from rest_framework.generics import (DestroyAPIView,
                                     ListAPIView)
from ..serializers.track_time import TrackTimeSerializer, TrackDeleteSerializer
from ...models import TrackTime
from rest_framework.permissions import IsAuthenticated
from ....abstract.functional import sanitize_query_params, get_user
from rest_framework.views import APIView
from ....user.models import EmployeeUser
from ...models import Issue
from rest_framework.response import Response
from rest_framework import status
from ...services import commit_minutes_statistics, track_and_record
from ....abstract.permissions import IsCreator, NonGuest
from datetime import date
from django.db.models import Sum
from ....abstract.exceptions import OverTimeException


class TrackCreateView(APIView):
    permission_classes = (IsAuthenticated, NonGuest)

    def post(self, request):
        data = request.data
        me = get_user(request)
        executor = EmployeeUser.objects.filter(user=request.user).first()
        minutes = data.get('minutes')
        text = data.get('text', '')

        if not minutes:
            return Response(data={"detail": "invalid time"}, status=status.HTTP_400_BAD_REQUEST)

        full_day = 60 * 8
        all_tracks_today = TrackTime.objects.filter(executor=executor, datetime__date=date.today()) \
            .aggregate(Sum('minutes'))
        all_tracks_today = all_tracks_today.get('minutes__sum', 0) or 0

        if full_day - all_tracks_today - minutes < 0:
            raise OverTimeException

        issue_id = data.get('issue_id')
        if issue_id:
            issue = Issue.objects.get(id=issue_id)
            TrackTime.objects.depend_create(me=me, issue=issue, minutes=minutes, executor=executor, text=text)
            commit_minutes_statistics(request, issue, minutes)
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
    permission_classes = (IsAuthenticated, IsCreator)
    serializer_class = TrackDeleteSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return TrackTime.objects.all()

    def delete(self, request, *args, **kwargs):
        me = get_user(request)
        track = self.get_object()
        issue = track.issue
        minutes = -track.minutes
        track_and_record(me, issue, minutes)
        commit_minutes_statistics(request, issue, minutes)
        return super().delete(request, *args, **kwargs)
