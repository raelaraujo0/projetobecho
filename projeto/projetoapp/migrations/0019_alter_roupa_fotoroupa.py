# Generated by Django 5.0 on 2024-01-25 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetoapp', '0018_roupa_nomebrecho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roupa',
            name='FotoRoupa',
            field=models.ImageField(blank=True, upload_to='fotosroupas/'),
        ),
    ]