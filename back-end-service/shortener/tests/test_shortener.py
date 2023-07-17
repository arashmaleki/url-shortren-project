from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from shortener.models import Shortener
from shortener.serializers import ShortenerSerializer
from url_shortener import settings
from users.models import User
from shortener.tests.mock_data import *


class ShortenerViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = User.objects.create_user(**admin_data)
        self.token = Token.objects.create(user=self.author)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        shortener_data['author_id'] = self.author.id
        shortener2_data['author_id'] = self.author.id
        self.shortener = Shortener.objects.create(**shortener_data)
        self.shortener2 = Shortener.objects.create(**shortener2_data)

    def test_get_shortener_list(self):
        url = reverse("shortener-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.data['results'][0]["long_url"], str(self.shortener.long_url))
        self.assertEqual(response.data['results'][1]["long_url"], str(self.shortener2.long_url))

    def test_get_shortener_detail(self):
        url = reverse("shortener-detail", args=[self.shortener.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = ShortenerSerializer(self.shortener)
        self.assertEqual(response.data, serializer.data)

    def test_create_shortener(self):
        url = reverse("shortener-list")
        response = self.client.post(url, create_shortener_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Shortener.objects.count(), 3)

    def test_update_shortener(self):
        url = reverse("shortener-detail", args=[self.shortener.id])
        response = self.client.put(url, update_shortener_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Shortener.objects.get(id=self.shortener.id).long_url,
            update_shortener_data["long_url"]
        )

    def test_delete_shortener(self):
        url = reverse("shortener-detail", args=[self.shortener.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Shortener.objects.count(), 1)

    def test_redirect(self):
        short_url = self.shortener.short_url.replace(settings.BASE_URL, '')
        url = reverse("redirect-shortener-url", args=[short_url])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['long_url'], self.shortener.long_url)
