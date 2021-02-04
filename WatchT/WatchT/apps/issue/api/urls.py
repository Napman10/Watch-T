from django.urls import path, include
from .views.issue import IssueListView, IssueOpenView, IssueCreateView, IssueDestroyView

update_issue_patterns = [
    path('', IssueOpenView.as_view()),
]

urlpatterns = [
    path('list', IssueListView.as_view()),
    path('<uuid:id>', include(update_issue_patterns)),
    path('new', IssueCreateView.as_view()),
    path('delete/<uuid:id>', IssueDestroyView.as_view()),
]
