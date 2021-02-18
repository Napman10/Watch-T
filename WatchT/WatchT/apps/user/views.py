from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .services import create_user
from .serializers import EmployeeUserSerializer
from .models import EmployeeUser
from ..abstract.functional import sanitize_query_params
from django.db.models.query import Q
from rest_framework.response import Response
from rest_framework import status


class UserSingleAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        return create_user(user_data=data)


class UserAPIListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        params = sanitize_query_params(request)
        somename = params.get('somename')

        if somename is not None:
            del params['somename']
            q1 = {**params, "user__username__contains": somename}
            q2 = {**params, "user__first_name__contains": somename}
            q3 = {**params, "user__last_name__contains": somename}
            qs = EmployeeUser.objects.filter(Q(**q1) | Q(**q2) | Q(**q3))
        elif bool(params):
            qs = EmployeeUser.objects.filter(**params)
        else:
            qs = EmployeeUser.objects.all()

        result = []

        for employee in qs:
            pure_user = employee.user
            result.append({"pure_user": {"username": pure_user.username, "first_name": pure_user.first_name,
                                         "last_name": pure_user.last_name, "email": pure_user.email},
                           "photo": employee.photo.path, "role": employee.role})

        serializer = EmployeeUserSerializer(data=result, many=True)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)
