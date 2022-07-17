from rest_framework import serializers
from bradocs4py.cnpj import ValidadorCnpj
from bradocs4py.cpf import ValidadorCpf


def validate_document(self, data):

    document_number = data.get('document_number')
    person_type = data.get('person_type')

    if not document_number.isnumeric():
        raise serializers.ValidationError({'Document Number': 'Please, type just numbers.'})

    if (len(document_number) != 11) and (len(document_number) != 14):
        raise serializers.ValidationError({'Document Number': 'Please, retype the document number.'})
    
    if (person_type == 'NP'): # NP = NATURAL_PERSON
        if (len(document_number) == 11):
            if ValidadorCpf.validar(document_number):
                return document_number
                
        raise serializers.ValidationError({'Document Number': 'Invalid Natural Person Document. Please retype.'})

    if (person_type == 'LP'): # LP = LEGAL_PERSON
        if (len(document_number) == 14):
            if ValidadorCnpj.validar(document_number):
                return document_number
                
        raise serializers.ValidationError({'Document Number': 'Invalid Legal Person Document. Please retype.'})
