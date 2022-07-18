"""
	Module containing the Test for the Account Model.
"""

from django.test import TestCase
from banking.models.account_model import AccountModel


class AccountModelTest(TestCase):
    """
    Class for the Tests of Account Model.
    """

    def setUp(self):
        """
        Creates Account objects to used in the tests.
        """

        # Given
        # Randomly generated valid numbers.
        AccountModel.objects.create(
            name="John Stone",
            document_number="34630412000",
            person_type="NP",
            balance=500,
        )

        AccountModel.objects.create(
            name="Lucy Stone",
            document_number="65352743063",
            person_type="NP",
            balance=580,
        )

        AccountModel.objects.create(
            name="Rest Cafe",
            document_number="97329380000144",
            person_type="LP",
            balance=5990,
        )

    def test_account_created(self):
        """
        Tests if a new account is being correctly created.
        """

        # When
        number_of_accounts = AccountModel.objects.count()

        # Then
        self.assertEqual(number_of_accounts, 3)
