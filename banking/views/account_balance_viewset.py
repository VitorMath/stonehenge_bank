"""
	Module containing the Account Balance Viewset.
"""

from rest_framework import generics
from banking.models.account_model import AccountModel
from banking.serializers.account_balance_serializer import AccountBalanceSerializer


class AccountBalanceViewset(generics.ListAPIView):
    """
    This class creates a ListAPIView to return the balance of a specific account.
    """

    def get_queryset(self):
        """
        This overrides the method get_queryset, returning a
        queryset filtered by the primary key of the Account Model.
        """
        queryset = AccountModel.objects.filter(id=self.kwargs["pk"])
        return queryset

    serializer_class = AccountBalanceSerializer
