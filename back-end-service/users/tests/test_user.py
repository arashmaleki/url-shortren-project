from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from users.models import User
from users.serializers import UserSerializer
from users.tests.mock_data import *


class UserViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.superuser = User.objects.create_superuser(**admin_data)
        self.token = Token.objects.create(user=self.superuser)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.user1 = User.objects.create(**user1_data)
        self.user2 = User.objects.create(**user2_data)

    def test_get_user_list(self):
        url = reverse("user-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.data['results'][1]["username"], str(self.user1.username))
        self.assertEqual(response.data['results'][2]["username"], str(self.user2.username))

    def test_get_user_detail(self):
        url = reverse("user-detail", args=[self.user1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = UserSerializer(self.user1)
        self.assertEqual(response.data, serializer.data)

    def test_update_user(self):
        url = reverse("user-detail", args=[self.superuser.id])
        response = self.client.patch(url, update_user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            User.objects.get(id=self.superuser.id).first_name,
            update_user_data["first_name"]
        )

    def test_delete_user(self):
        url = reverse("user-detail", args=[self.superuser.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 2)
