# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 13:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0004_auto_20160528_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='representative',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poll.Club'),
        ),
    ]