from django.urls import include, path

from .views import RegisterUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view())
]
