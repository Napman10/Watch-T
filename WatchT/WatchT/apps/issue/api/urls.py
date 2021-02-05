from django.urls import include, path

from .views.issue import (IssueCreateView, IssueDestroyView, IssueListView,
                          IssueOpenView)

update_issue_patterns = [
    path('', IssueOpenView.as_view()),
]

urlpatterns = [
    path('list', IssueListView.as_view()),
    path('<uuid:id>', include(update_issue_patterns)),
    path('new', IssueCreateView.as_view()),
    path('delete/<uuid:id>', IssueDestroyView.as_view()),
]
