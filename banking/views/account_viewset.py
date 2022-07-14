from rest_framework import viewsets
from rest_framework import permissions
from banking.models.account_model import AccountModel
from banking.serializers.account_serializer import AccountSerializer


class AccountViewset(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = AccountModel.objects.all()
    # permission_classes = [permissions.IsAuthenticated]