# Generated by Django 2.1 on 2019-01-25 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20190121_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True),
        ),
    ]
