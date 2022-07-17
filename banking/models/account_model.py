from django.db import models

class AccountModel(models.Model):

    TYPE_CHOICES = [('NP', 'NATURAL_PERSON'), ('LP', 'LEGAL_PERSON')]

    name = models.CharField(max_length=100, default='name')
    document_number = models.CharField(max_length=14, help_text='Just Numbers', unique=True, default=0)
    person_type = models.CharField(
        verbose_name='Person Type', max_length=2, choices=TYPE_CHOICES, default='NP'
    )
    balance =  models.PositiveIntegerField(default=0, editable=False)
