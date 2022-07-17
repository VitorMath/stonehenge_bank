from rest_framework import serializers
from banking.models.account_model import AccountModel
from banking.validators.validate_document import validate_document


class AccountSerializer(serializers.HyperlinkedModelSerializer):

    class Meta():
        model = AccountModel
        fields = "__all__"


    def validate(self, data):
        # validate_document(self, data.get('document_number'),
        #                         data.get('person_type'))

        validate_document(self, data)

        return data
