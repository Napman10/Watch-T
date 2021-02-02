from django.contrib import admin
from .models import User, User2Team, Team


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'role', 'first_name', 'last_name']


@admin.register(User2Team)
class User2TeamAdmin(admin.ModelAdmin):
    list_display = ['team', 'user']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name']
