# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 13:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0005_auto_20160528_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='board',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='poll.Board'),
        ),
        migrations.AlterField(
            model_name='club',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
