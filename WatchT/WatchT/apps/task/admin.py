from django.contrib import admin
from .models import Task, Project, Comment


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'project', 'author', 'executor']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'team']


admin.register(Comment)
