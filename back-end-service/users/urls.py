from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from users.views import (UserRegisterAPIView, UserListAPIView, UserDetailAPIView)


urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('', UserListAPIView.as_view(), name='user-list'),
    path('<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
]
