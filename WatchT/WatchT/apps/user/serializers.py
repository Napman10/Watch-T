from rest_framework import serializers

from .models import EmployeeUser


class EmployeeUserSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = EmployeeUser
        fields = ('email', 'username', 'first_name', 'last_name', 'password', 'photo', 'role')
        extra_kwargs = {'password': {'write_only': True}}
