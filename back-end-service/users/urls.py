from django.urls import path
from users.views import (UserRegisterAPIView, UserListAPIView, UserDetailAPIView, UserLoginAPIView)


urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('', UserListAPIView.as_view(), name='user-list'),
    path('<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
]
