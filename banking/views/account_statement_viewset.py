"""
	Module containing the Account Statement Viewset.
"""

from django.db.models import Q
from rest_framework import generics
from rest_framework import filters
from banking.models.transaction_model import TransactionModel
from banking.serializers.account_statement_serializer import AccountStatementSerializer


class AccountStatementViewset(
    generics.ListAPIView
):  # generics.ListAPIView -  viewsets.ModelViewSet
    """
    This class creates a ListAPIView to list all transactions sent and
    received by an spefied account, creating the bank statement.
    It possible to filter the transactions by date. To do so, query
    parameters must be sent in the request, using ISO 8601 standard format.

    start_date -> date and time that the transactions filtered will start from.

    end_date -> date and time that the transactions filtered will end.

    Example: http://127.0.0.1:8000/account/16/statement/
        ?start_date=2022-07-17T20:57:36.018929-03:00
        &end_date=2022-07-17T20:57:47.328983-03:00
    """

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["date"]
    ordering_fields = ["date"]

    def get_queryset(self):
        """
        This overrides the method get_queryset, returning a
        queryset filtered by the primary key of the Account Model
        and if parameters passed, by start and end date.
        """

        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")

        queryset = TransactionModel.objects.filter(
            Q(debited_account=self.kwargs["pk"]) | Q(credited_account=self.kwargs["pk"])
        ).order_by("date")

        if start_date:
            queryset = queryset.filter(date__gte=start_date)

        if end_date:
            queryset = queryset.filter(date__lte=end_date)

        return queryset

    serializer_class = AccountStatementSerializer
