# Generated by Django 2.1 on 2019-02-07 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carteira', '0002_auto_20190207_1052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carteira',
            old_name='saldo_carteira',
            new_name='saldo',
        ),
    ]
