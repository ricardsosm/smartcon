# Generated by Django 2.1 on 2019-02-02 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_auto_20190125_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='id_carteira',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]