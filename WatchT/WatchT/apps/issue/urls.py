from django.urls import path, include
from .views import IssueListView, IssueOpenView, IssueCreateView

urlpatterns = [
    path('list', IssueListView.as_view()),
    path('<uuid:id>', IssueOpenView.as_view()),
    path('new', IssueCreateView.as_view()),
]
