# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20171024_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='status',
            field=models.CharField(choices=[('a', 'assignments'), ('b', 'plans'), ('c', 'current'), ('d', 'done')], max_length=45),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='ttc',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
    ]