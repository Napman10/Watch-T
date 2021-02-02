from django.urls import path, include
from .views import IssueView

urlpatterns = [
    path('', IssueView.as_view())
]