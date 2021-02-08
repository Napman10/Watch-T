from django.contrib import admin
from django.contrib.auth.models import Group

from .models import EmployeeUser


@admin.register(EmployeeUser)
class EmployeeUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'role']


admin.site.unregister(Group)
