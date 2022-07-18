"""
	Module containing the Tests for the Transaction Methods.
"""

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from banking.models.account_model import AccountModel


class TransactionMethodsTest(TestCase):
    """
    Class for the Tests of Transaction Methods.
    """

    def setUp(self) -> None:
        """
        Sets up APIClient for the tests.
        """

        self.client = APIClient()

        # Given
        # Randomly generated valid numbers.
        self.account_one = AccountModel.objects.create(
            name="John Stone",
            document_number="34630412000",
            person_type="NP",
            balance=500,
        )
        self.account_two = AccountModel.objects.create(
            name="Rest Cafe",
            document_number="97329380000144",
            person_type="LP",
            balance=0,
        )

    def test_account_post(self):
        """
        Tests if a POST method is working correctly.
        """

        # When
        transaction = {
            "amount": 50,
            "debited_account": f"http://127.0.0.1:8000/account/{self.account_one.id}/",
            "credited_account": f"http://127.0.0.1:8000/account/{self.account_two.id}/",
        }

        response = self.client.post("/transaction/", transaction, format="json")

        # Then
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_account_get(self):
        """
        Tests if a GET method is working correctly.
        """

        # When
        response = self.client.get("/transaction/")

        # Then
        self.assertEqual(response.status_code, 200)
