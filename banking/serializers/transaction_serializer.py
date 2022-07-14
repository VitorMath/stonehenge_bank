from rest_framework import serializers
from banking.models.transaction_model import TransactionModel


class TransactionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta():
        model = TransactionModel
        fields = "__all__"
