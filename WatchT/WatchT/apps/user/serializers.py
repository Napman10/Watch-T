from rest_framework import serializers
from django.conf import settings
from .models import EmployeeUser
import os


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=150)
    first_name = serializers.CharField(max_length=30, allow_blank=True)
    last_name = serializers.CharField(max_length=150, allow_blank=True)


class EmployeeUserSerializer(serializers.Serializer):
    pure_user = UserSerializer()
    role = serializers.IntegerField()
    photo = serializers.CharField()
