# Generated by Django 2.1 on 2019-02-28 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0005_auto_20190221_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='ativo',
            field=models.BooleanField(),
        ),
    ]
