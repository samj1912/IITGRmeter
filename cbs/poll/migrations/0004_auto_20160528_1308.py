# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 13:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_auto_20160528_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='representative',
            name='club',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='poll.Club'),
        ),
    ]
