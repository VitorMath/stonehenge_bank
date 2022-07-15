from rest_framework.test import APIClient
from rest_framework import status

from django.test import TestCase
from banking.models.account_model import AccountModel
from banking.models.transaction_model import TransactionModel


class AccountStatementTest(TestCase):

    def setUp(self):
        # Given
        self.client = APIClient()

        account_one = AccountModel.objects.create(balance=500)
        account_two = AccountModel.objects.create()

        TransactionModel.objects.create(debited_account = account_one,
                                        credited_account = account_two,
                                        amount = 200
        )

        TransactionModel.objects.create(debited_account = account_two,
                                        credited_account = account_one,
                                        amount = 80
        )


    def test_statement_get(self):

        # When
        accounts = AccountModel.objects.all().values('id')

        id_account_one = accounts[0].get('id')

        response = self.client.get(f'/account/{id_account_one}/statement/')

        # Then
        self.assertTrue(response.json()) # Test if the JSON is not empty
