from django.test import TestCase
from rest_framework.test import APIClient
import json


# Create your tests here.


class UserRegisterTest1(TestCase):

    def setUp(self):
        self.user_info = {
            "name": "test",
            "password": "123456",
            "email": "123456@qq.com"
        }

    def test_register(self):
        client = APIClient()
        response = client.post("/api/user/register/", data=self.user_info, format='json')
        print(response)
        self.assertEqual(response.status_code, 201)
