# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-07 14:33
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_auto_20170207_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='last_clicks',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), blank=True, default=None, null=True, size=10),
        ),
    ]
