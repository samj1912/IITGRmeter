# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0014_representative_sub_board'),
    ]

    operations = [
        migrations.AddField(
            model_name='representative',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b'images/'),
        ),
    ]
