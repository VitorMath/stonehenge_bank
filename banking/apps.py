"""
	Module containing the BankingConfig class.
"""
from django.apps import AppConfig


class BankingConfig(AppConfig):
    """
    Class that sets some configuration for the Banking app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "banking"
