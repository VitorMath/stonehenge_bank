"""
	Module containing the models that are registered for the admin control panel.
"""

from django.contrib import admin
from .models.account_model import AccountModel
from .models.transaction_model import TransactionModel

admin.site.register(AccountModel)
admin.site.register(TransactionModel)
