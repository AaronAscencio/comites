# Generated by Django 4.1.7 on 2023-05-02 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seccion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipio',
            name='nombre',
            field=models.CharField(max_length=150),
        ),
    ]
