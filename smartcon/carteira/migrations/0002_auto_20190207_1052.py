# Generated by Django 2.1 on 2019-02-07 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carteira', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carteira',
            name='private_key',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Chave Privada'),
        ),
        migrations.AddField(
            model_name='carteira',
            name='public_key',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Chave Privada'),
        ),
    ]
