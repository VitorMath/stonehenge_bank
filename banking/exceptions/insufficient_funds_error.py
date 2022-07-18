"""
	Module containing the Base Banking Error.
"""

from banking.exceptions.base_banking_error import BaseBankingError
from rest_framework import status


class InsufficientFundsError(BaseBankingError):
    """
        Class containing the Insufficient Funds Error, that is called when an
    account has not enough funds to perform the transaction requested.
    """

    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_detail = "Not enought funds."
    default_code = "Insufficient Funds Error"
