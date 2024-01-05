# Generated by Django 5.0 on 2024-01-05 17:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetoapp', '0010_cliente_roupa_comprada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roupa',
            name='Preco',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
