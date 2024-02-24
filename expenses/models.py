from django.contrib.auth.models import User
from django.db import models


class Portions(models.Model):
    date = models.DateField(verbose_name="Date")
    portion = models.PositiveSmallIntegerField(verbose_name="Current Portion")
    max_portion = models.PositiveSmallIntegerField(verbose_name="Portion Quantity")


class Expenses(models.Model):
    TYPE_CHOICES = {
        "FIXO": "FIXO",
        "VARIAVEL": "VARIAVEL",
    }
    date = models.DateField(verbose_name="Date")
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, verbose_name="Expense Type")
    value = models.FloatField(verbose_name="Value")
    is_entry = models.BooleanField(default=False, verbose_name="Is Entry")
    name = models.CharField(max_length=100, verbose_name="Name")
    portions = models.CharField(max_length=10, verbose_name="Portion")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    portions_id = models.ForeignKey(Portions, on_delete=models.SET_NULL, null=True)
