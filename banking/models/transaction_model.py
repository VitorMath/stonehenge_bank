"""
	Module containing the Transaction Model.
"""

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from banking.exceptions.insufficient_funds_error import InsufficientFundsError
from banking.models.account_model import AccountModel


class TransactionModel(models.Model):
    """
        Class that defines the Transaction dataset model, where transactions
    info are saved.
    Its attributes are:

    debited_account -> a ForeignKey that refers to the account that will
    be debited the funds.

    credited_account -> a ForeignKey that refers to the account that will
    be credited the funds.

    amount -> an IntegerField that contains the amount of cents that will
    be transferred from debited_account to credited_account.

    date -> a DateTimeField that saves the exact moment when the
    transaction is made. It used the ISO 8601 international standard of
    date and time-related data.
    """

    debited_account = models.ForeignKey(
        AccountModel, on_delete=models.CASCADE, related_name="debited_account"
    )
    credited_account = models.ForeignKey(
        AccountModel, on_delete=models.CASCADE, related_name="credited_account"
    )
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)


@receiver(pre_save, sender=TransactionModel, dispatch_uid="update_balance")
def check_enough_balance(sender, instance, **kwargs):

    """
    This function is called just before a new transaction is saved (created or
    updated) and is responsible for cheking if the debited account has enough
    funds to make the transaction.
    """

    if instance.debited_account.balance < instance.amount:
        raise InsufficientFundsError({"Amount": "Not enough funds in the account."})


@receiver(post_save, sender=TransactionModel, dispatch_uid="update_balance")
def update_balance(sender, instance, **kwargs):

    """
    This function is called just after a new transaction is saved (created or
    updated) and is responsible for updating the balances of both debited and
    credited accounts.
    """

    instance.debited_account.balance -= instance.amount
    instance.credited_account.balance += instance.amount

    instance.debited_account.save()
    instance.credited_account.save()
