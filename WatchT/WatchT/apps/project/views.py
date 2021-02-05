from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveUpdateAPIView)

from .models import Project
from .serializers import ProjectSerializer


class ProjectListView(ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()


class ProjectOpenView(RetrieveUpdateAPIView):
    serializer_class = ProjectSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Project.objects.all()


class ProjectCreateView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    action_map = {
        'post': 'create'
    }


class ProjectDestroyView(DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'
    action_map = {
        'delete': 'delete'
    }
