from django.urls import path
from shortener.views import ShortenerCreateApiView, ShortenerDetailAPIView, ShortenerRedirectAPIView

urlpatterns = [
    path('', ShortenerCreateApiView.as_view(), name='shortener-list'),
    path('<int:pk>', ShortenerDetailAPIView.as_view(), name='shortener-detail'),
    path('redirect/<str:short_url>', ShortenerRedirectAPIView.as_view(), name='redirect-shortener-url'),
]
