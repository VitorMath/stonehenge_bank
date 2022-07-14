from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class AccountMethodsTest(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()


    def test_account_post(self):
        # Given
        account = {"balance": 1}

        # When
        response = self.client.post('/account/', account, format='json')

        # Then
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_account_get(self):

        # When
        response = self.client.get('/account/')

        # Then
        self.assertEqual(response.status_code, 200)
