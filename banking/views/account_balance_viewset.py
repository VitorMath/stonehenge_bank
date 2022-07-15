from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from banking.models.account_model import AccountModel
from banking.serializers.account_balance_serializer import AccountBalanceSerializer


class AccountBalanceViewset(generics.ListAPIView):

    def get_queryset(self):
        queryset = AccountModel.objects.filter(id=self.kwargs['pk'])
        return queryset

    serializer_class = AccountBalanceSerializer
