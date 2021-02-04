from django.contrib import admin
from .models import EmployeeUser


@admin.register(EmployeeUser)
class EmployeeUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active', 'role']
