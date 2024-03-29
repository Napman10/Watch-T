from rest_framework import serializers

from ..abstract.functional import convert_last_seen
from .models import EmployeeUser, UserStatistics


class EmployeeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeUser
        fields = ('id', 'role', 'first_name', 'last_name', 'email', 'username', 'level')

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


class UserStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStatistics
        fields = ('joined', 'tracked_minutes')

    joined = serializers.SerializerMethodField()

    def get_joined(self, obj: UserStatistics) -> str:
        return convert_last_seen(obj.joined)
