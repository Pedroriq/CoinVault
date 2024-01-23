from django.contrib.auth.models import User
from django.db import models


class Parcelas(models.Model):
    date = models.DateField(verbose_name='Data')
    portion = models.PositiveSmallIntegerField(verbose_name='Parcela Atual')
    max_portion = models.PositiveSmallIntegerField(verbose_name='Quantidade de Parcelas')


class Gastos(models.Model):
    TYPE_CHOICES = {
        'FIXO': 'FIXO',
        'INVESTIMENTO': 'INVESTIMENTO',
        'VARIAVEL': 'VARIAVEL',
    }
    date = models.DateField(verbose_name='Data')
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, verbose_name='Tipo de Gastos')
    value = models.FloatField(verbose_name='Valor')
    is_entry = models.BooleanField(default=False, verbose_name='Entrada')
    name = models.CharField(max_length=100, verbose_name='Nome')
    portions = models.CharField(max_length=10, verbose_name='Parcela')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    parcelas_id = models.ForeignKey(Parcelas, on_delete=models.SET_NULL, null=True)
