# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-15 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0004_auto_20180414_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='day',
            field=models.CharField(choices=[('M', 'Monday'), ('Tu', 'Tuesday'), ('W', 'Wednesday'), ('Th', 'Thursday'), ('F', 'Friday'), ('Sa', 'Saturday'), ('Su', 'Sunday')], max_length=1),
        ),
    ]