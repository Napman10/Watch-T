from django.urls import path

from .views import (MissingSkillsListView, OpenMe, UserAPIListView,
                    UserCreateAPIView, UserOpenView, UserStatisticsView)

urlpatterns = [
    path('', UserCreateAPIView.as_view()),
    path('list/', UserAPIListView.as_view()),
    path('<uuid:id>', UserOpenView.as_view()),
    path('statistics/<uuid:id>', UserStatisticsView.as_view()),
    path('missing_skills/', MissingSkillsListView.as_view()),
    path('me', OpenMe.as_view()),
]
