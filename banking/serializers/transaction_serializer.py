from enum import unique
from rest_framework import serializers
from banking.models.transaction_model import TransactionModel


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    amount = serializers.IntegerField(min_value=1)

    class Meta():
        model = TransactionModel
        fields = "__all__"

    def validate(self, data):
        if data.get('debited_account') == data.get('credited_account'):
            raise serializers.ValidationError({'Debited and Credited Accounts': 'Accounts must be different!'})

        return data
