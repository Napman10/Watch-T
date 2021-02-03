from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Team
from .serializers import TeamSerializer


class TeamListView(ListAPIView):
    serializer_class = TeamSerializer

    def get_queryset(self):
        return Team.objects.all()


class TeamOpenView(RetrieveUpdateAPIView):
    serializer_class = TeamSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Team.objects.all()


class TeamCreateView(CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    action_map = {
        'post': 'create'
    }


class TeamDestroyView(DestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = 'id'
    action_map = {
        'delete': 'delete'
    }

