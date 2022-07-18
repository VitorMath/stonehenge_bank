"""
	Module containing the Account Model Serializer.
"""

from rest_framework import serializers
from banking.models.account_model import AccountModel
from banking.validators.validate_document import validate_document


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class creates a HyperlinkedModelSerializer that serializes
    accounts to the database.

    Sets the balance attributes as read only.

    Raises -> ValidationError
    """

    balance = serializers.IntegerField(read_only=True)

    class Meta:
        """
        This class sets the AccountModel to be the model serialized and
        defines that all fields will be used.
        """

        model = AccountModel
        fields = "__all__"

    def validate(self, data):
        """
        This method call the validate_document function that validates
        documents numeration.
        """

        validate_document(self, data)

        return data
