"""
	Module containing the Account Viewset.
"""

from rest_framework import viewsets
from banking.models.account_model import AccountModel
from banking.serializers.account_serializer import AccountSerializer


class AccountViewset(viewsets.ModelViewSet):
    """
    This class creates a ModelViewSet for the Account Serializer.
    """

    serializer_class = AccountSerializer
    queryset = AccountModel.objects.all()
