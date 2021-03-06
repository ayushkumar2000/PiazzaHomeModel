# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-10 13:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filetype', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=5000)),
                ('author', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('filetype', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.thread'),
        ),
    ]
