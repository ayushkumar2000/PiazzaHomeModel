# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-01 21:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0011_resource_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='author',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='created',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='rfile',
        ),
    ]
