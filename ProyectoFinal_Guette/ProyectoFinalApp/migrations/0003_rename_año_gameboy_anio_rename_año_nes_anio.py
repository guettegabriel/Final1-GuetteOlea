# Generated by Django 4.0.5 on 2022-06-28 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoFinalApp', '0002_rename_año_sega_anio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gameboy',
            old_name='año',
            new_name='anio',
        ),
        migrations.RenameField(
            model_name='nes',
            old_name='año',
            new_name='anio',
        ),
    ]
