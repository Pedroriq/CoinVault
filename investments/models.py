from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Investimento(models.Model):
    TYPE_CHOICES = {
        'FIIs': 'FUNDO IMOBILIÁRIO (FII)',
        'CDB': 'CERTIFICADO DE DEPÓSITO BANCÁRIO (CDB)',
        'ACAO': 'AÇÃO',
        'CRIPTO': 'CRIPTOMOEDA',
    }
    date = models.DateField(verbose_name='Data')
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, verbose_name='Tipo de Investimento')
    value = models.FloatField(verbose_name='Valor')
    name = models.CharField(max_length=100, verbose_name='Nome do Investimento')
    profitability = models.FloatField(verbose_name='Rentabilidade')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
