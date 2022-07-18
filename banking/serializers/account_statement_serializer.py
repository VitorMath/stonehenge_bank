"""
	Module containing the Account Statement Serializer.
"""

from rest_framework import serializers
from banking.models.transaction_model import TransactionModel


class AccountStatementSerializer(serializers.ModelSerializer):
    """
    This class creates a ModelSerializer that serializes and return a
    statement of all transactions sent and received by an account.
    """

    class Meta:
        """
        This class sets the TransactionModel to be the model serialized and
        defines that all fields will be returned.
        """

        model = TransactionModel
        fields = "__all__"
