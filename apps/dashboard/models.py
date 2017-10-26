# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Import models from Django
from django.db import models
from ..landing.models import Member

# Import time ops
import datetime


# Models: Assignment, Goal, Scorecard 

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
    track = models.CharField(max_length=45, choices=TRACKS)
    status = models.CharField(max_length=45, choices=LANE)
    title = models.CharField(max_length=45)
    on_time = models.BooleanField(default=False) # calculate from duration
    optional = models.BooleanField(default=False)

    # measurements for calculations
    points = models.IntegerField()
    est_duration = models.DurationField()
    act_duration = models.DurationField(blank=True)
    time_mult = models.DecimalField(max_digits=3, decimal_places=1)
    start_time = models.DateTimeField(auto_now_add=True) # required
    end_time = models.DateTimeField(auto_now_add=True) # required

class Goal(models.Model): # goals persist over workdays until done
    member = models.ForeignKey(Member, related_name="goals", on_delete=models.CASCADE)
    desc = models.CharField(max_length=200)
    status = models.CharField(max_length=45)
    added = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField()

class Scorecard(models.Model):
    member = models.ForeignKey(Member, related_name="scorecards", on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    potential = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    actual = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # use scorecards to calculate running total, and find average


# Add points color via style class (set classes to 1-5)

# CURRENTLY WORKING:
# - show list of others working on same assignment, encourage pair programming
# - show assignment page for people to discuss on there...