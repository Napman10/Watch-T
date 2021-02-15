
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .services import create_user


class UserAPI(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        return create_user(user_data=data)
