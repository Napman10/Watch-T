from django.urls import include, path

from .views import (ProjectCreateView, ProjectDestroyView, ProjectListView,
                    ProjectOpenView)

urlpatterns = [
    path('list', ProjectListView.as_view()),
    path('<uuid:id>', ProjectOpenView.as_view()),
    path('new', ProjectCreateView.as_view()),
    path('delete/<uuid:id>', ProjectDestroyView.as_view()),
]
