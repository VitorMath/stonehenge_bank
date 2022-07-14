from rest_framework import serializers
from banking.models.account_model import AccountModel


class AccountSerializer(serializers.HyperlinkedModelSerializer):

    class Meta():
        model = AccountModel
        fields = "__all__"
