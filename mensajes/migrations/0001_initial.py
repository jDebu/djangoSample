# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-09 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('dni', models.CharField(max_length=50)),
                ('nombres', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
            ],
        ),
    ]