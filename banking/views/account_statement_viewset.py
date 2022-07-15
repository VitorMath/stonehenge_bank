from django.db.models import Q
from rest_framework import generics
from rest_framework import filters
from banking.models.transaction_model import TransactionModel
from banking.serializers.account_statement_serializer import AccountStatementSerializer

class AccountStatementViewset(generics.ListAPIView): # generics.ListAPIView -  viewsets.ModelViewSet

    """ Returns a statement of the account, with received and sent transactions. """

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['date']
    ordering_fields = ['date']

    def get_queryset(self):

        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        queryset = TransactionModel.objects.filter(
            Q(debited_account=self.kwargs['pk'])
            | Q(credited_account=self.kwargs['pk'])).order_by('date')

        if start_date:
            queryset = queryset.filter(date__gte=start_date)
        
        if end_date:
            queryset = queryset.filter(date__lte=end_date)

        return queryset

    serializer_class = AccountStatementSerializer
