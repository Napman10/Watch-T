from django.urls import path, include
from .views import IssueListView, IssueOpenView, IssueCreateView, IssueDestroyView

urlpatterns = [
    path('list', IssueListView.as_view()),
    path('<uuid:id>', IssueOpenView.as_view()),
    path('new', IssueCreateView.as_view()),
    path('delete/<uuid:id>', IssueDestroyView.as_view()),
]
