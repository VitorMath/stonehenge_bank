from django.db import models

class AccountModel(models.Model):
    balance =  models.PositiveIntegerField(default=0) # IntegerField(default=0)
    