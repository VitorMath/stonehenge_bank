from datetime import datetime
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from banking.models.account_model import AccountModel


class TransactionMethodsTest(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

        # Given
        self.account_one = AccountModel.objects.create(balance=500)
        self.account_two = AccountModel.objects.create()


    def test_account_post(self):

        # When
        transaction = {
            "amount": 50,
            "debited_account": f"http://127.0.0.1:8000/account/{self.account_one.id}/",
            "credited_account": f"http://127.0.0.1:8000/account/{self.account_two.id}/",
            }
        
        response = self.client.post('/transaction/',transaction, format='json')

        print(response)

        # Then
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_account_get(self):

        # When
        response = self.client.get('/transaction/')

        # Then
        self.assertEqual(response.status_code, 200)
