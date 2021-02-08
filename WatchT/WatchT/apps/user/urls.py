from django.urls import include, path

from .views import (CreateUserAPIView, UserRetrieveUpdateAPIView,
                    authenticate_user, logout)

urlpatterns = [
    path('create/', CreateUserAPIView.as_view()),
    path('obtain_token/', authenticate_user),
    path('update/', UserRetrieveUpdateAPIView.as_view()),
    path('logout/', logout),
]
