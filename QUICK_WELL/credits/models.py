from django.db import models

class Balance(models.Model):
    userid = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=30, null=False)
    balance = models.FloatField(null=False, default=0)

class Pay(models.Model):
    userid = models.IntegerField()
    key = models.CharField(max_length=8)
    amount = models.IntegerField()
