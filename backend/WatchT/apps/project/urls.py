from django.urls import path

from .views import (ProjectCreateView, ProjectDestroyView, ProjectListView,
                    ProjectOpenView, Project2UserView, ProjectStatisticsView)

urlpatterns = [
    path('list', ProjectListView.as_view()),
    path('<uuid:id>', ProjectOpenView.as_view()),
    path('new', ProjectCreateView.as_view()),
    path('delete/<uuid:id>', ProjectDestroyView.as_view()),
    path('assign/', Project2UserView.as_view()),
    path('statistics/<uuid:id>', ProjectStatisticsView.as_view()),
]
