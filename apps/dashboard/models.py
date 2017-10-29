# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..landing.models import User

from datetime import timedelta


class Session(models.Model):
    user = models.ForeignKey(User, related_name="sessions", on_delete=models.CASCADE)
    potential = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    actual = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    start = models.DateTimeField(default=None, blank=True, null=True)
    end = models.DateTimeField(default=None, blank=True, null=True)
    est_duration = models.DurationField(default=timedelta())
    time_bonus = models.DurationField(default=timedelta())
    time_challenge = models.DurationField(default=timedelta())
    act_duration = models.DurationField(default=timedelta())
    on_time = models.BooleanField(default=False)


class Assignment(models.Model):

    TRACKS = (
        ('pyfun1', 'Python Fundamentals 1'),
        ('pyfun2', 'Python Fundamentals 2'),
        ('pyoop', 'Python OOP'),
        ('flask1', 'Flask Fundamentals'),
        ('mysql', 'MySQL'),
        ('flask2', 'Flask with MySQL'),
        ('django', 'Django'),
        ('djangoorm', 'Django ORM'),
        ('javafun', 'Java Fundamentals'),
        ('javaoop', 'Java OOP'),
        ('javaspring1', 'Java Spring 1'),
        ('javaspringdata', 'Java Spring Data'),
        ('javaspring2', 'Java Spring 2'),
    )

    LANE = (
        ('a', 'assignments'),
        ('b', 'plans'),
        ('c', 'commit'),
        ('d', 'current'),
        ('e', 'done'),
        ('f', 'display')
    )

    user = models.ForeignKey(User, related_name="assignments", on_delete=models.CASCADE)
    session = models.ForeignKey(Session, related_name="assignments", blank=True, null=True)
    track = models.CharField(max_length=45, choices=TRACKS)
    status = models.CharField(max_length=45, choices=LANE, default='a')
    title = models.CharField(max_length=45)
    pageid = models.CharField(max_length=45)
    optional = models.BooleanField(default=False)

    # measurements for calculations
    base_points = models.IntegerField()
    time_mult = models.DecimalField(max_digits=3, decimal_places=1)
    est_duration = models.DurationField(default=timedelta())

    # to update via events
    potential = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    act_duration = models.DurationField(default=timedelta())
    on_time = models.BooleanField(default=False) # calculate from duration
    actual = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)


