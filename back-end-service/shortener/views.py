from django.shortcuts import get_object_or_404, redirect
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from shortener.models import Shortener
from shortener.serializers import ShortenerSerializer
from django.conf import settings
from shortener.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from shortener.pagination import CustomPagination


class ShortenerCreateApiView(generics.ListCreateAPIView):
    serializer_class = ShortenerSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = Shortener.objects.filter(author=self.request.user).all().order_by('click_count')
        return queryset


class ShortenerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shortener.objects.all()
    serializer_class = ShortenerSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            queryset = Shortener.objects.filter(author=self.request.user).all()
            return queryset


class ShortenerRedirectAPIView(RetrieveAPIView):
    serializer_class = ShortenerSerializer

    def get(self, request, short_url, *args, **kwargs):
        short_link = settings.BASE_URL + self.kwargs['short_url']
        shortened_instance = get_object_or_404(Shortener, short_url=short_link)
        shortened_instance.click_count += 1
        shortened_instance.save()
        serializer = self.get_serializer(shortened_instance)
        return Response(serializer.data)

