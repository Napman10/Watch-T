from django.urls import include, path
from .views import UserSingleAPI, UserAPIListView

urlpatterns = [
    path('', UserSingleAPI.as_view()),
    path('list/', UserAPIListView.as_view())
]
