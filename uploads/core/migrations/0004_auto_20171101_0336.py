# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-10-31 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_document_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='media/'),
        ),
    ]
