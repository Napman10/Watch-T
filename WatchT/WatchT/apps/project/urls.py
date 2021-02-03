from django.urls import path, include
from .views import ProjectListView, ProjectOpenView, ProjectCreateView, ProjectDestroyView

urlpatterns = [
    path('list', ProjectListView.as_view()),
    path('<uuid:id>', ProjectOpenView.as_view()),
    path('new', ProjectCreateView.as_view()),
    path('delete/<uuid:id>', ProjectDestroyView.as_view()),
]
