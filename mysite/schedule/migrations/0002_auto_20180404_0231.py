# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-04 07:31
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
