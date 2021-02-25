from django.contrib import admin
from django.contrib.auth.models import Group

from .models import EmployeeUser

admin.site.register(EmployeeUser)
admin.site.unregister(Group)
