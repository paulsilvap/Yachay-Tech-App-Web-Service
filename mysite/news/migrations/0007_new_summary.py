# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-12 23:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20180228_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='summary',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
    ]
