# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-17 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_thread_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='created',
            field=models.DateTimeField(),
        ),
    ]
