# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-20 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_auto_20180420_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='image',
            field=models.FileField(default='null', upload_to='images'),
        ),
    ]