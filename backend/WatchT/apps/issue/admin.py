from django.contrib import admin

from .models import Comment, Issue, IssueHistoryRecord, IssueType, TrackTime


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'project', 'author', 'executor']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'issue', 'text', 'datetime']


@admin.register(TrackTime)
class TrackTimeAdmin(admin.ModelAdmin):
    list_display = ['issue', 'executor', 'minutes', 'text']


admin.site.register(IssueType)


@admin.register(IssueHistoryRecord)
class IssueHistoryRecordAdmin(admin.ModelAdmin):
    list_display = ['issue', 'datetime']
