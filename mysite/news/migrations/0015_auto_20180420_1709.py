# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-20 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_auto_20180420_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='image',
            field=models.FileField(default='null', upload_to='127.0.0.1:8000/media/images'),
        ),
    ]