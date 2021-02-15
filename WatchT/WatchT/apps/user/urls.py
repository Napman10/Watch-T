from django.urls import include, path
from .views import UserAPI

urlpatterns = [
    path('', UserAPI.as_view()),
]
