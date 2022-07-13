from django.db import models

class AccountModel(models.Model):
    balance =  models.IntegerField(default=0)
    