from django.contrib import admin
from .models import User2Team, Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(User2Team)
class User2TeamAdmin(admin.ModelAdmin):
    list_display = ['team', 'user']
