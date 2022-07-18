"""
	Module containing the Test for the Account Statement.
"""

from rest_framework.test import APIClient
from django.test import TestCase
from banking.models.account_model import AccountModel
from banking.models.transaction_model import TransactionModel


class AccountStatementTest(TestCase):
    """
    Class for the Tests of Account Statement.
    """

    def setUp(self):
        """
        Sets up APIClient and Creates Account and Transaction objects
        to used in the tests.
        """

        # Given
        self.client = APIClient()

        # Randomly generated valid numbers.
        account_one = AccountModel.objects.create(
            name="John Stone",
            document_number="34630412000",
            person_type="NP",
            balance=500,
        )
        account_two = AccountModel.objects.create(
            name="Rest Cafe",
            document_number="97329380000144",
            person_type="LP",
            balance=0,
        )

        TransactionModel.objects.create(
            debited_account=account_one, credited_account=account_two, amount=200
        )

        TransactionModel.objects.create(
            debited_account=account_two, credited_account=account_one, amount=80
        )

    def test_statement_get(self):
        """
        Tests if a GET method is working correctly.
        """

        # When
        accounts = AccountModel.objects.all().values("id")

        id_account_one = accounts[0].get("id")

        response = self.client.get(f"/account/{id_account_one}/statement/")

        # Then
        self.assertTrue(response.json())  # Test if the JSON is not empty
