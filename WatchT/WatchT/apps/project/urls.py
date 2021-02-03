from django.urls import path, include
from .views import ProjectListView, ProjectOpenView, ProjectCreateView

urlpatterns = [
    path('list', ProjectListView.as_view()),
    path('<uuid:id>', ProjectOpenView.as_view()),
    path('new', ProjectCreateView.as_view()),
]
