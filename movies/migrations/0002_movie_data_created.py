# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-27 16:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='data_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
