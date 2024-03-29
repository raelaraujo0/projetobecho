# Generated by Django 5.0 on 2024-01-23 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetoapp', '0016_alter_roupa_fotoroupa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='cliente_comprou',
        ),
        migrations.RemoveField(
            model_name='venda',
            name='roupa_comprada',
        ),
        migrations.AddField(
            model_name='venda',
            name='cliente_comprou',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projetoapp.roupa'),
        ),
        migrations.AddField(
            model_name='venda',
            name='roupa_comprada',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projetoapp.cliente'),
        ),
    ]
