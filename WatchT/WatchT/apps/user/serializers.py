from rest_framework import serializers

from .models import EmployeeUser


class EmployeeUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeUser
        fields = ('user', 'photo', 'role')
