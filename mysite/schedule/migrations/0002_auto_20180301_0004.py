# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-01 05:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schedule',
            options={'ordering': ('name',)},
        ),
    ]
