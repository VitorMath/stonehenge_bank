from rest_framework import serializers
from banking.models.account_model import AccountModel

class AccountBalanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountModel
        fields = [
            'id',
            'balance',
        ]
