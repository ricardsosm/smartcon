# Generated by Django 2.1 on 2019-01-25 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_auto_20190125_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='id_carteira',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]