from django.urls import include, path

from .views.issue import (IssueCreateView, IssueDestroyView, IssueListView,
                          IssueOpenView)
from .views.comment import CommentListView

update_issue_patterns = [
    path('', IssueOpenView.as_view()),
]

comment_patterns = [
    path('list/', CommentListView.as_view())
]

urlpatterns = [
    path('comment/', include(comment_patterns)),
    path('list', IssueListView.as_view()),
    path('<uuid:id>', include(update_issue_patterns)),
    path('new', IssueCreateView.as_view()),
    path('delete/<uuid:id>', IssueDestroyView.as_view()),
]
