from django.urls import path
from .views import TeamListView, TeamOpenView, TeamCreateView, TeamDestroyView

urlpatterns = [
    path('list', TeamListView.as_view()),
    path('<uuid:id>', TeamOpenView.as_view()),
    path('new', TeamCreateView.as_view()),
    path('delete/<uuid:id>', TeamDestroyView.as_view()),
]
