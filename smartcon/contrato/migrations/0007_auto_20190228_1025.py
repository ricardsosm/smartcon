# Generated by Django 2.1 on 2019-02-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0006_auto_20190228_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='ativo',
            field=models.BooleanField(null=True),
        ),
    ]