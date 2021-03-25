from django.contrib import admin
from django.contrib.auth.models import Group

from .models import EmployeeUser, UserStatistics


@admin.register(UserStatistics)
class UserStatisticsAdmin(admin.ModelAdmin):
    list_display = ['user']


admin.site.register(EmployeeUser)
admin.site.unregister(Group)
