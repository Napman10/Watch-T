from rest_framework import serializers
from .models import EmployeeUser


class EmployeeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeUser
        fields = ('id', 'photo', 'role', 'first_name', 'last_name', 'email', 'username',)

    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    def get_first_name(self, obj: EmployeeUser) -> str:
        return str(obj.user.first_name)

    def get_last_name(self, obj: EmployeeUser) -> str:
        return str(obj.user.last_name)

    def get_username(self, obj: EmployeeUser) -> str:
        return str(obj)

    def get_email(self, obj: EmployeeUser) -> str:
        return str(obj.user.email)
