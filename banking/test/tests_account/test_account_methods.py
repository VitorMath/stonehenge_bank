"""
	Module containing the Tests for the Account Methods.
"""

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class AccountMethodsTest(TestCase):
    """
    Class for the Tests of Account Methods.
    """

    def setUp(self) -> None:
        """
        Sets up APIClient for the tests.
        """

        self.client = APIClient()

    def test_account_post(self):
        """
        Tests if a POST method is working correctly.
        """

        # Given
        account = {
            "name": "John Stone",
            "document_number": "34630412000",  # Randomly generated valid number.
            "person_type": "NP",
            "balance": 1,
        }

        # When
        response = self.client.post("/account/", account, format="json")

        # Then
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_account_get(self):
        """
        Tests if a GET method is working correctly.
        """

        # When
        response = self.client.get("/account/")

        # Then
        self.assertEqual(response.status_code, 200)
