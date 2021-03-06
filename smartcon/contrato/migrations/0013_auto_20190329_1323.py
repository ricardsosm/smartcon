# Generated by Django 2.1 on 2019-03-29 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carteira', '0006_carteira_id_token'),
        ('contrato', '0012_contrattoken_contract_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contrato',
            name='wallet_address',
        ),
        migrations.RemoveField(
            model_name='contrato',
            name='wallet_private_key',
        ),
        migrations.AddField(
            model_name='contrato',
            name='id_carteira',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='carteira.Carteira', verbose_name='Carteira'),
            preserve_default=False,
        ),
    ]
