# Generated by Django 4.1.7 on 2023-05-01 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(unique=True, verbose_name='Numero')),
            ],
            options={
                'verbose_name': 'Distrito',
                'verbose_name_plural': 'Distritos',
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, unique=True)),
                ('distrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seccion.distrito')),
            ],
            options={
                'verbose_name': 'Municipio',
                'verbose_name_plural': 'Municipios',
            },
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(unique=True, verbose_name='Seccion')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seccion.municipio')),
            ],
            options={
                'verbose_name': 'Seccion',
                'verbose_name_plural': 'Secciones',
            },
        ),
        migrations.CreateModel(
            name='Colonia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre')),
                ('tipo', models.CharField(max_length=50, verbose_name='Tipo')),
                ('seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seccion.seccion')),
            ],
            options={
                'verbose_name': 'Colonia',
                'verbose_name_plural': 'Colonias',
            },
        ),
    ]
