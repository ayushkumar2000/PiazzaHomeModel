# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-01 20:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_resource'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='title',
            field=models.CharField(default='hello', max_length=1000),
            preserve_default=False,
        ),
    ]
