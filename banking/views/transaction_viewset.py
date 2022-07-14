from rest_framework import viewsets
from rest_framework import permissions
from banking.models.transaction_model import TransactionModel
from banking.serializers.transaction_serializer import TransactionSerializer


class TransactionViewset(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = TransactionModel.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
