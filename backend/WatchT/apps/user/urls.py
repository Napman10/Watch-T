from django.urls import path

from .views import (MissingSkillsListView, OpenMe, UserAPIListView,
                    UserCreateAPIView, UserOpenView, UserStatisticsView, AssignmentProblem)

urlpatterns = [
    path('', UserCreateAPIView.as_view()),
    path('list/', UserAPIListView.as_view()),
    path('<uuid:id>', UserOpenView.as_view()),
    path('statistics/<uuid:id>', UserStatisticsView.as_view()),
    path('missing_skills/', MissingSkillsListView.as_view()),
    path('assignment_problem/', AssignmentProblem.as_view()),
    path('me', OpenMe.as_view()),
]
