from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView)
from .models import Project, Project2User, ProjectStatistics
from .serializers import ProjectSerializer, ProjectStatisticsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException
from ..user.models import EmployeeUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from ..abstract.functional import sanitize_query_params
from ..issue.models import Issue
from ..abstract.permissions import AssignedStuffOnly, IsAdmin, IsCreator, AdminEditProject
from .services import filter_projects, edit_project, initialize_user_project_pair, delete_p2u


class ProjectListView(ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return filter_projects(self.request)


class ProjectOpenView(RetrieveUpdateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, AssignedStuffOnly, AdminEditProject)
    lookup_field = 'id'

    def get_queryset(self):
        return Project.objects.all()

    def put(self, request, *args, **kwargs):
        edit_project(self.get_object())
        return Response(status=status.HTTP_200_OK)


class ProjectCreateView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, IsAdmin)

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        returned_id = response.data.get('id')
        project = Project.objects.get(id=returned_id)
        ProjectStatistics.objects.create(project=project)

        return response


class ProjectDestroyView(DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, IsAdmin)
    lookup_field = 'id'


class Project2UserView(APIView):
    permission_classes = (IsAuthenticated, IsCreator)

    def post(self, request):
        user, project = initialize_user_project_pair(request)
        Project2User.objects.create(user=user, project=project)
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request):
        delete_p2u(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProjectStatisticsView(RetrieveAPIView):
    serializer_class = ProjectStatisticsSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return Project.objects.all()

    def get_object(self):
        project = super().get_object()
        return ProjectStatistics.objects.filter(project=project).first()
