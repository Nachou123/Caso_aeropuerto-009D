# Generated by Django 4.0.5 on 2022-07-11 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='idcliente',
            new_name='rut',
        ),
    ]