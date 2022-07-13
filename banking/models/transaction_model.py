from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from banking.models.account_model import AccountModel

class TransactionModel(models.Model):
    debited_account = models.ForeignKey(AccountModel,
                                        on_delete=models.PROTECT,
                                        related_name='debited_account')
    credited_account = models.ForeignKey(AccountModel,
                                        on_delete=models.PROTECT,
                                        related_name='credited_account') 
    amount = models.IntegerField() # amount of cents to be transfered
    date = models.DateTimeField(auto_now_add=True) # date of creation


@receiver(post_save, sender=TransactionModel, dispatch_uid="update_balance")
def update_stock(sender, instance, **kwargs):

    instance.debited_account.balance -= instance.amount
    instance.credited_account.balance += instance.amount

    instance.debited_account.save()
    instance.credited_account.save()
    