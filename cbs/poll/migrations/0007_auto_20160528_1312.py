# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 13:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0006_auto_20160528_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='board',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poll.Board'),
        ),
        migrations.AlterField(
            model_name='club',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
