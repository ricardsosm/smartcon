# Generated by Django 2.1 on 2019-03-01 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0009_auto_20190301_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='ativo',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]