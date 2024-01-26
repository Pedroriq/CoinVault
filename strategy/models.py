from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Strategy(models.Model):
    variable_expenses = models.FloatField(verbose_name="Variable Expenses")
    fixed_expenses = models.FloatField(verbose_name="Fixed Expenses")
    investments = models.FloatField(verbose_name="Investments")
    name = models.CharField(verbose_name="Name", max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
