from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Estrategia(models.Model):
    variable_expenses = models.FloatField(verbose_name="Custos Variáveis")
    fixed_expenses = models.FloatField(verbose_name="Custos Fixos")
    investiments = models.FloatField(verbose_name="Investimentos")
    name = models.CharField(verbose_name="Nome", max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
