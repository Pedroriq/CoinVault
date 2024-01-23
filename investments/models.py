from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Investment(models.Model):
    TYPE_CHOICES = {
        "FIIs": "FUNDO IMOBILIÁRIO (FII)",
        "CDB": "CERTIFICADO DE DEPÓSITO BANCÁRIO (CDB)",
        "ACAO": "AÇÃO",
        "CRIPTO": "CRIPTOMOEDA",
    }
    date = models.DateField(verbose_name="Date")
    type = models.CharField(
        max_length=100,
        choices=TYPE_CHOICES,
        verbose_name="Investment Type",
    )
    value = models.FloatField(verbose_name="Value")
    name = models.CharField(max_length=100, verbose_name="Investment Name")
    profitability = models.FloatField(verbose_name="Profitability")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
