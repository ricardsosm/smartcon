# Generated by Django 2.1 on 2019-01-30 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_remove_usuario_salt'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='ip_actual',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(blank=True, default=False, verbose_name='Esta ativo'),
        ),
    ]
