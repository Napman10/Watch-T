from django.urls import include, path
from .views import UserCreateAPIView, UserAPIListView, UserOpenView

urlpatterns = [
    path('', UserCreateAPIView.as_view()),
    path('list/', UserAPIListView.as_view()),
    path('<uuid:id>', UserOpenView.as_view()),
]
