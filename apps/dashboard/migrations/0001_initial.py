# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 19:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('track', models.CharField(choices=[('PyFun', 'Python Fundamentals'), ('PyOOP', 'Python OOP'), ('Flask', 'Python: Flask')], max_length=1)),
                ('status', models.CharField(choices=[('a', 'listed'), ('b', 'agenda'), ('c', 'current'), ('d', 'done')], max_length=1)),
                ('time_est', models.IntegerField()),
                ('completed', models.DateTimeField()),
                ('time_taken', models.IntegerField()),
                ('difficulty', models.IntegerField()),
                ('optional', models.BooleanField(default=False)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to=settings.AUTH_USER_MODEL)),
                ('pair', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pair_assignment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=45)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('completed', models.DateTimeField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goals', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Scorecard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_avg', models.IntegerField()),
                ('weekly_avg', models.IntegerField()),
                ('time_vs_est', models.IntegerField()),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]