# Generated by Django 5.0.1 on 2024-02-01 20:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("investments", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Investment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("date", models.DateField(verbose_name="Date")),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("FIIs", "FUNDO IMOBILIÁRIO (FII)"),
                            ("CDB", "CERTIFICADO DE DEPÓSITO BANCÁRIO (CDB)"),
                            ("ACAO", "AÇÃO"),
                            ("CRIPTO", "CRIPTOMOEDA"),
                        ],
                        max_length=100,
                        verbose_name="Investment Type",
                    ),
                ),
                ("value", models.FloatField(verbose_name="Value")),
                ("name", models.CharField(max_length=100, verbose_name="Investment Name")),
                ("profitability", models.FloatField(verbose_name="Profitability")),
                (
                    "user_id",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Investimento",
        ),
    ]