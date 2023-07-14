from rest_framework import serializers
from .models import Shortener


class ShortenerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Shortener
        fields = "__all__"
