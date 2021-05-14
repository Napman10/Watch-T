from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .services import create_user, edit_user, filter_users
from .serializers import EmployeeUserSerializer, UserStatisticsSerializer
from .models import EmployeeUser, UserStatistics, Skill
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from ..abstract.functional import sanitize_query_params, get_user, get_user_dict
from django.db.models.query import Q
from rest_framework.response import Response
from rest_framework import status
from ..project.models import Project2User
from ..abstract.permissions import IsAdmin, NonAdminChange
from ..issue.models import IssueType
from ..issue.api.serializers.issue import IssueTypeSerializer


class UserCreateAPIView(APIView):
    permission_classes = (IsAuthenticated, IsAdmin)

    def post(self, request):
        data = request.data
        return create_user(user_data=data)


class UserOpenView(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeUserSerializer
    permission_classes = (IsAuthenticated, NonAdminChange)
    lookup_field = 'id'

    def get_queryset(self):
        return EmployeeUser.objects.all()

    def put(self, request, *args, **kwargs):
        edit_user(request, self.get_object())
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        pure_user = user.user
        pure_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MissingSkillsListView(ListAPIView):
    permission_classes = (IsAuthenticated, IsAdmin)
    serializer_class = IssueTypeSerializer

    def get_queryset(self):
        params = sanitize_query_params(self.request)
        user_id = params.get('id')
        skills = Skill.objects.filter(employee__id=user_id)
        skills = [skill.skill.typo for skill in skills]
        return IssueType.objects.exclude(typo__in=skills)


class UserAPIListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EmployeeUserSerializer

    def get_queryset(self):
        return filter_users(self.request)


class OpenMe(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = get_user(request)
        user_dict = get_user_dict(user)

        return Response(status=status.HTTP_200_OK, data=user_dict)


class UserStatisticsView(RetrieveAPIView):
    serializer_class = UserStatisticsSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return EmployeeUser.objects.all()

    def get_object(self):
        user = super().get_object()
        return UserStatistics.objects.filter(user=user).first()
