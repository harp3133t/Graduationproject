# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-11-12 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20171104_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('count', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]
