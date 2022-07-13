from django.test import TestCase
from banking.models.account_model import AccountModel


class AccountTestCase(TestCase):
    

    def setUp(self):
        # Given
        AccountModel.objects.create(balance=500)

        AccountModel.objects.create(balance=580)

        AccountModel.objects.create(balance=5990)


    def test_account_created(self):

        # When
        number_of_accounts = AccountModel.objects.count()

        # Then
        self.assertEqual(number_of_accounts, 3)
