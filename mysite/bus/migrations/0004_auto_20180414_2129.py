# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-15 02:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0003_auto_20180414_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop', models.CharField(max_length=200)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.Schedule')),
            ],
        ),
        migrations.DeleteModel(
            name='Stops',
        ),
    ]