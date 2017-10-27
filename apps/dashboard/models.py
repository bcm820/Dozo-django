# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Import models from Django
from django.db import models
from ..landing.models import Member

# Import time ops
import datetime


class Assignment(models.Model):

    TRACKS = (
        ('a', 'Python Fundamentals'),
        ('b', 'Python: Django'),
    )

    LANE = (
        ('a', 'assignments'),
        ('b', 'plans'),
        ('c', 'commit'),
        ('d', 'current'),
        ('e', 'done'),
        ('f', 'display')
    )

    member = models.ForeignKey(Member, related_name="assignments", on_delete=models.CASCADE)
    scorecard = models.ForeignKey(Scorecard, related_name="assignments", blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)
    track = models.CharField(max_length=45, choices=TRACKS)
    status = models.CharField(max_length=45, choices=LANE)
    title = models.CharField(max_length=45)
    optional = models.BooleanField(default=False)

    # measurements for calculations
    base_points = models.IntegerField()
    time_mult = models.DecimalField(max_digits=3, decimal_places=1)
    est_duration = models.DurationField()

    # to update via events
    potential = models.DecimalField(max_digits=10, decimal_places=2)
    start_time = models.DateTimeField(auto_now_add=True) # required
    end_time = models.DateTimeField(auto_now_add=True) # required
    act_duration = models.DurationField(blank=True)
    on_time = models.BooleanField(default=False) # calculate from duration
    actual = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class Goal(models.Model): # goals persist until done
    
    GOALS = (
        ('c', 'commit'),
        ('d', 'current'),
        ('e', 'done'),
        ('f', 'display')
    )
    
    member = models.ForeignKey(Member, related_name="goals", on_delete=models.CASCADE)
    desc = models.CharField(max_length=200)
    status = models.CharField(max_length=45, choices=GOALS)
    started = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(auto_now=False, auto_now_add=False)


class Scorecard(models.Model):
    member = models.ForeignKey(Member, related_name="scorecards", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)
    potential = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    actual = models.DecimalField(max_digits=10, decimal_places=2, default=0)