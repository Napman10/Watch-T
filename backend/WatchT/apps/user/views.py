from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .services import create_user
from .serializers import EmployeeUserSerializer
from .models import EmployeeUser
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from ..abstract.functional import sanitize_query_params, get_user, get_user_dict
from ..abstract.exceptions import NotConfirmedPass
from django.db.models.query import Q
from rest_framework.response import Response
from rest_framework import status
from ..project.models import Project2User
from ..abstract.permissions import IsAdmin


class UserCreateAPIView(APIView):
    permission_classes = (IsAuthenticated, IsAdmin)

    def post(self, request):
        data = request.data
        return create_user(user_data=data)


class UserOpenView(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeUserSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return EmployeeUser.objects.all()

    def put(self, request, *args, **kwargs):
        data = request.data
        user = self.get_object()
        real_user = user.user

        username = data.get('username')
        if username:
            real_user.username = username
            real_user.save()

        first_name = data.get('first_name')
        if first_name:
            real_user.first_name = first_name
            real_user.save()

        last_name = data.get('last_name')
        if last_name:
            real_user.last_name = last_name
            real_user.save()

        email = data.get('email')
        if email:
            real_user.email = email
            real_user.save()

        role = data.get('role')
        if role:
            user.role = role
            user.save()

        password = data.get('password')
        confirm = data.get('password2')

        if password != confirm and password:
            raise NotConfirmedPass
        if password:
            real_user.set_password(password)
            real_user.save()

        return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        pure_user = user.user
        pure_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPIListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EmployeeUserSerializer

    def get_queryset(self):
        params = sanitize_query_params(self.request)
        project_id = params.get('project_id')
        dev = params.get('dev')
        if project_id is not None:
            exclude = params.get('exclude')
            p2u = Project2User.objects.filter(project__id=project_id)
            user_ids = [p.user.id for p in p2u]
            if exclude is not None:
                return EmployeeUser.objects.exclude(id__in=user_ids)
            if dev is not None:
                return EmployeeUser.objects.filter(id__in=user_ids,
                                                   role__in=[EmployeeUser.DEVELOPER,
                                                             EmployeeUser.ADMINISTRATOR,
                                                             EmployeeUser.LEAD])
            return EmployeeUser.objects.filter(id__in=user_ids)

        somename = params.get('somename')

        if somename is not None:
            del params['somename']
            q1 = {**params, "user__username__contains": somename}
            q2 = {**params, "user__first_name__contains": somename}
            q3 = {**params, "user__last_name__contains": somename}
            return EmployeeUser.objects.filter(Q(**q1) | Q(**q2) | Q(**q3))
        elif bool(params):
            return EmployeeUser.objects.filter(**params)
        else:
            return EmployeeUser.objects.all()


class OpenMe(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = get_user(request)
        user_dict = get_user_dict(user)

        return Response(status=status.HTTP_200_OK, data=user_dict)
