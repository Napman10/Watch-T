from django.contrib import admin
from .models import Issue, Comment


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'project', 'author', 'executor']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'issue', 'text', 'edited', 'datetime']
