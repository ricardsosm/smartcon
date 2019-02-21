# Generated by Django 2.1 on 2019-02-21 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0004_contrato_abi'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='ativo',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='id_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente', verbose_name='Cliente'),
        ),
    ]