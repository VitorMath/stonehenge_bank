from rest_framework import serializers
from banking.models.transaction_model import TransactionModel

class AccountStatementSerializer(serializers.ModelSerializer):
    # id = serializers.ReadOnlyField(source='account.id')
    # balance = serializers.ReadOnlyField(source='account.balance')

    class Meta:
        model = TransactionModel
        fields = "__all__"