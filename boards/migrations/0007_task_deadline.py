# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-19 19:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]