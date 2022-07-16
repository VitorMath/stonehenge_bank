from banking.exceptions.base_banking_error import BaseBankingError
from rest_framework import status


class InsufficientFundsError(BaseBankingError):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_detail = 'Not enought funds.'
    default_code = 'Insufficient Funds Error'
