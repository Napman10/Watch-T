from django.urls import include, path

from .views.issue import (IssueCreateView, IssueDestroyView, IssueListView,
                          IssueOpenView, IssueChildListView)
from .views.comment import CommentListView, CommentOpenView, CommentCreateView, CommentDeleteView
from .views.track_time import TrackCreateView, TrackListView,  TrackDeleteView

single_comment_patterns = [
    path('', CommentOpenView.as_view()),
    path('delete', CommentDeleteView.as_view()),
]

comment_patterns = [
    path('<uuid:id>/', include(single_comment_patterns)),
    path('list/', CommentListView.as_view()),
    path('new/', CommentCreateView.as_view()),
]

single_track_patterns = [
    path('delete', TrackDeleteView.as_view()),
]

track_patterns = [
    path('<uuid:id>/', include(single_track_patterns)),
    path('create/', TrackCreateView.as_view()),
    path('list/', TrackListView.as_view()),
]

urlpatterns = [
    path('comment/', include(comment_patterns)),
    path('track/', include(track_patterns)),

    path('<uuid:id>/', IssueOpenView.as_view()),
    path('list', IssueListView.as_view()),
    path('new', IssueCreateView.as_view()),
    path('delete/<uuid:id>', IssueDestroyView.as_view()),
    path('childlist', IssueChildListView.as_view()),
]
