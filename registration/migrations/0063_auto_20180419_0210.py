# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-19 06:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0062_auto_20180416_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='firebase',
            name='cashdrawer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='firebase',
            name='token',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='order',
            name='billingType',
            field=models.CharField(choices=[('Unpaid', 'Unpaid'), ('Credit', 'Credit'), ('Cash', 'Cash'), ('Comp', 'Comp')], default='Credit', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.Discount'),
        ),
        migrations.AlterField(
            model_name='pricelevel',
            name='priceLevelOptions',
            field=models.ManyToManyField(blank=True, to='registration.PriceLevelOption'),
        ),
    ]