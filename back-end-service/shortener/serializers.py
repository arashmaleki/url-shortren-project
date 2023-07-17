from rest_framework import serializers
from url_shortener import settings
from .models import Shortener


class ShortenerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Shortener
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update({"short_url": f'{settings.BASE_URL}{data["short_url"]}'})
        return data
