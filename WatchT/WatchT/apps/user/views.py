from django.contrib.auth.models import User
from .models import EmployeeUser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class UserAPI(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data

        role = data.get('role')

        password = data.get('password')
        password_confirm = data.get('password2')

        if bool(password) and password != password_confirm:
            return Response({"detail": "password dismatch"}, status=status.HTTP_400_BAD_REQUEST)

        del data['password2']
        del data['role']

        try:
            username = data.get('username')
            if User.objects.filter(username=username).exists():
                return Response({"detail": f"{username} already exists"}, status=status.HTTP_400_BAD_REQUEST)

            original_user = User.objects.create_user(**data)
            EmployeeUser.objects.create(user=original_user, role=role)
        except BaseException as e:
            return Response({"detail": e}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"username": original_user.username, "detail": "registration successful"},
                        status=status.HTTP_200_OK)
