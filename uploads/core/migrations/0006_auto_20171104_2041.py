# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-11-04 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20171104_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='name',
        ),
        migrations.AddField(
            model_name='document',
            name='author',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
