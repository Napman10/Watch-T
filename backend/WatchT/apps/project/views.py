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
from ..abstract.functional import sanitize_query_params
from ..issue.models import Issue
from ..abstract.permissions import AssignedStuffOnly, MustBeAdmin


class ProjectListView(ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Project.objects.all()


class ProjectOpenView(RetrieveUpdateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, AssignedStuffOnly)
    lookup_field = 'id'

    def get_queryset(self):
        return Project.objects.all()


class ProjectCreateView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, MustBeAdmin)

    def post(self, request, *args, **kwargs):
        pure_user = request.user
        user = EmployeeUser.objects.filter(user=pure_user).first()

        response = super().post(request, *args, **kwargs)
        returned_id = response.data.get('id')
        project = Project.objects.get(id=returned_id)
        Project2User.objects.create(project=project, user=user)

        return response


class ProjectDestroyView(DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'
    action_map = {
        'delete': 'delete'
    }


class Project2UserView(APIView):
    permission_classes = (IsAuthenticated,)

    def initialize(self, request):
        data = request.data
        if not data:
            data = sanitize_query_params(request)
        username = data.get('user')
        if not username:
            raise APIException
        project_id = data.get('project_id')
        if not project_id:
            raise APIException
        user = EmployeeUser.objects.filter(user__username=username).first()
        project = Project.objects.get(id=project_id)
        return user, project

    def post(self, request):
        user, project = self.initialize(request)
        Project2User.objects.create(user=user, project=project)
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request):
        user, project = self.initialize(request)
        p = Project2User.objects.filter(user=user, project=project).first()
        if p:
            project = p.project
            issues = Issue.objects.filter(project=project)
            for issue in issues:
                issue.executor = None
                issue.save()
            p.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
