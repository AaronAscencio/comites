# Generated by Django 4.1.7 on 2023-06-18 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seccion', '0003_remove_colonia_tipo_colonia_cp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colonia',
            name='cp',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Codigo Postal'),
        ),
    ]
