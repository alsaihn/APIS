# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-25 00:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0074_staff_checkedin'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealer',
            name='logo',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
