from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveUpdateAPIView)
from .models import Project, Project2User
from .serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException
from ..user.models import EmployeeUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class ProjectListView(ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Project.objects.all()


class ProjectOpenView(RetrieveUpdateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return Project.objects.all()


class ProjectCreateView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)

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


class Project2UserView(APIView):

    def initialize(self, request):
        data = request.data
        user_id = data.get('user_id')
        if not user_id:
            raise APIException
        project_id = data.get('project_id')
        if not project_id:
            raise APIException
        user = EmployeeUser.objects.get(id=user_id)
        project = Project.objects.get(id=project_id)
        return user, project

    def post(self, request):
        user, project = self.initialize(request)
        Project2User.objects.create(user=user, project=project)
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request):
        user, project = self.initialize(request)
        Project2User.objects.filter(user=user, project=project).first().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
