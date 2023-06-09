# Generated by Django 4.1.7 on 2023-06-27 07:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folio',
            name='numero',
            field=models.PositiveIntegerField(help_text='Ingresa un número entre 5 y 7 dígitos', unique=True, validators=[django.core.validators.MinValueValidator(10000, 'El número debe tener al menos 5 dígitos'), django.core.validators.MaxValueValidator(9999999, 'El número no puede tener más de 7 dígitos')], verbose_name='Numero de Folio'),
        ),
    ]
