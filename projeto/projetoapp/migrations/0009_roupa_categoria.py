# Generated by Django 5.0 on 2024-01-05 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetoapp', '0008_tamanho_remove_roupa_tamanho_roupa_tamanhos'),
    ]

    operations = [
        migrations.AddField(
            model_name='roupa',
            name='Categoria',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
