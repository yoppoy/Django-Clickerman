# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='bundle',
            name='total_clickers',
            field=models.IntegerField(default=-1),
        ),
    ]
