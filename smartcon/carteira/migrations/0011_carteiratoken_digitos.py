# Generated by Django 2.1 on 2019-05-08 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carteira', '0010_carteiratoken_contract'),
    ]

    operations = [
        migrations.AddField(
            model_name='carteiratoken',
            name='digitos',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]