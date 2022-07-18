"""
	Module containing the Transaction Model Serializer.
"""

from rest_framework import serializers
from banking.models.transaction_model import TransactionModel


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class creates a HyperlinkedModelSerializer that serializes
    all transactions saved in the database.

    amount -> defines that the field amount must has the minimuum value
    of 1 cent.

    Raises -> ValidationError
    """

    amount = serializers.IntegerField(min_value=1)

    class Meta:
        """
        This class sets the TransactionModel to be the model serialized and
        defines that all fields will be returned.
        """

        model = TransactionModel
        fields = "__all__"

    def validate(self, data):
        """
        This method validates that the debited and credited accounts are
        not the same.
        """
        if data.get("debited_account") == data.get("credited_account"):
            raise serializers.ValidationError(
                {"Debited and Credited Accounts": "Accounts must be different!"}
            )

        return data
