from django.contrib import admin
from .models.account_model import AccountModel
from .models.transaction_model import TransactionModel

admin.site.register(AccountModel)
admin.site.register(TransactionModel)
