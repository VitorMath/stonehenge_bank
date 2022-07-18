"""
	Module containing the Account Model.
"""

from django.db import models


class AccountModel(models.Model):
    """
        Class that defines the Account dataset model, where customer info and
    balance is saved.
    Its attributes are:

    name -> a Char Field that contains name of the customer.

    document_number -> a Char Field that must be unique in the database
    and represents the numeration of customer document.

    person_type -> a CharField that indicates the type of person the
    customer is. There are two options, Natural Person or Legal Person.

    balance -> an IntegerField that represent the amount of funds the
    customer currently has. It is expressed in cents, so one full unit of
    the fiat money will be express as 100.
    """

    TYPE_CHOICES = [("NP", "NATURAL_PERSON"), ("LP", "LEGAL_PERSON")]

    name = models.CharField(max_length=100, default="name")
    document_number = models.CharField(
        max_length=14, help_text="Just Numbers", unique=True, default=0
    )
    person_type = models.CharField(
        verbose_name="Person Type", max_length=2, choices=TYPE_CHOICES, default="NP"
    )
    balance = models.PositiveIntegerField(default=0)

    def __str__(self):
        """
        This method overrides the __str__ method of the AccountModel
        to set its representation in graphic interfaces as its id, plus
        its name and document attributes.
        """
        representation = f"{self.id} - {self.name} - {self.document_number}"

        return representation
