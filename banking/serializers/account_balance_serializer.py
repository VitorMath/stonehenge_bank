"""
	Module containing the Account Balance Serializer.
"""

from rest_framework import serializers
from banking.models.account_model import AccountModel


class AccountBalanceSerializer(serializers.ModelSerializer):
    """
    This class creates a ModelSerializer for the Account model balance.
    """

    class Meta:
        """
        This class sets the AccountModel to be the model serialized and
        defines the that fields id and balance will be returned.
        """

        model = AccountModel
        fields = [
            "id",
            "balance",
        ]
