from django.contrib import admin
from .models import Issue, Project, Comment


@admin.register(Issue)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'project', 'author', 'executor']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'team']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'issue', 'text', 'edited', 'datetime']
