from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .services import create_user
from .serializers import EmployeeUserSerializer
from .models import EmployeeUser
from rest_framework.generics import ListAPIView
from ..abstract.functional import sanitize_query_params
from django.db.models.query import Q
from rest_framework.response import Response
from rest_framework import status


class UserSingleAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        return create_user(user_data=data)


class UserAPIListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EmployeeUserSerializer

    def get_queryset(self):
        params = sanitize_query_params(self.request)
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
