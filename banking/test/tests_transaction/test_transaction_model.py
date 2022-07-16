from django.test import TestCase
from banking.models.account_model import AccountModel
from banking.models.transaction_model import TransactionModel


class TransactionModelTest(TestCase):
    
    def setUp(self):
        # Given
        self.account_one = AccountModel.objects.create(balance=500)
        self.account_two = AccountModel.objects.create()

        TransactionModel.objects.create(debited_account = self.account_one,
                                        credited_account = self.account_two,
                                        amount = 200
        )

        TransactionModel.objects.create(debited_account = self.account_two,
                                        credited_account = self.account_one,
                                        amount = 80
        )


    def test_transaction_created(self):
        # When
        number_of_transactions = TransactionModel.objects.count()

        # Then
        self.assertEqual(number_of_transactions, 2)
        
        
    def test_balance_update(self):
        # When
        balances = AccountModel.objects.all().values('balance')

        balance_one = balances[0].get('balance')
        balance_two = balances[1].get('balance')

        # Then
        self.assertTrue(balance_one == 380 and balance_two == 120)


    def test_enough_balance(self):
        """
        Test if system will block transaction creation when debited account
        has not enough balance.
        """

        # When
        TransactionModel.objects.create(debited_account = self.account_one,
                                        credited_account = self.account_two,
                                        amount = 800000000
        )

        balances = AccountModel.objects.all().values('balance')
        balance_one = balances[0].get('balance')

        # Then
        self.assertGreater(balance_one, 0)
        