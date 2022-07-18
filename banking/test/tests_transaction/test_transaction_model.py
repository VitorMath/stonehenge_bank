"""
	Module containing the Tests for the Transaction Model.
"""

from django.test import TestCase
from banking.models.account_model import AccountModel
from banking.models.transaction_model import TransactionModel


class TransactionModelTest(TestCase):
    """
    Class for the Tests of Transaction Model.
    """

    def setUp(self):
        """
        Creates Account and Transaction objects to used in the tests.
        """

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

        TransactionModel.objects.create(
            debited_account=self.account_one,
            credited_account=self.account_two,
            amount=200,
        )

        TransactionModel.objects.create(
            debited_account=self.account_two,
            credited_account=self.account_one,
            amount=80,
        )

    def test_transaction_created(self):
        """
        Tests if a transaction is being correctly created.
        """

        # When
        number_of_transactions = TransactionModel.objects.count()

        # Then
        self.assertEqual(number_of_transactions, 2)

    def test_balance_update(self):
        """
        Tests if the balance is being correctly updated.
        """

        # When
        balances = AccountModel.objects.all().values("balance")

        balance_one = balances[0].get("balance")
        balance_two = balances[1].get("balance")

        # Then
        self.assertTrue(balance_one == 380 and balance_two == 120)

    def test_enough_balance(self):
        """
        Test if system will block transaction creation when debited account
        has not enough balance.
        """

        # When
        try:
            TransactionModel.objects.create(
                debited_account=self.account_one,
                credited_account=self.account_two,
                amount=800000000,
            )
        except:
            pass  # If the system is working well, this test must always raise
            # an exception, so it's ok to keep this ppass statement here.

        balances = AccountModel.objects.all().values("balance")
        balance_one = balances[0].get("balance")

        # Then
        self.assertGreater(balance_one, 0)
