from django.contrib import admin

from .models import Project, Project2User, ProjectStatistics


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'header']


@admin.register(Project2User)
class Project2UserAdmin(admin.ModelAdmin):
    list_display = ['project', 'user']


@admin.register(ProjectStatistics)
class ProjectStatisticsAdmin(admin.ModelAdmin):
    list_display = ['project']
