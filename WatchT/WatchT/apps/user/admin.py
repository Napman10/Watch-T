from django.contrib import admin
from .models import CustomUser, User2Team, Team


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['role', 'user']


@admin.register(User2Team)
class User2TeamAdmin(admin.ModelAdmin):
    list_display = ['team', 'user']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name']
