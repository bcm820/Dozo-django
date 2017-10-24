# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Import models from Django
from django.db import models
from ..landing.models import Member


class Assignment(models.Model):
    TRACKS = (
        ('PyFun', 'Python Fundamentals'),
        ('PyOOP', 'Python OOP'),
        ('Flask', 'Python: Flask'),
    )
    LANE = (
        ('a', 'listed'),
        ('b', 'agenda'),
        ('c', 'current'),
        ('d', 'done')
    )
    member = models.ForeignKey(Member, related_name="assignments")
    pair = models.ForeignKey(Member, related_name="pair_assignment")
    title = models.CharField(max_length=45)
    track = models.CharField(max_length=1, choices=TRACKS)
    status = models.CharField(max_length=1, choices=LANE)
    time_est = models.IntegerField()
    completed = models.DateTimeField()
    time_taken = models.IntegerField()
    difficulty = models.IntegerField()
    optional = models.BooleanField(default=False)

class Goal(models.Model): # goals persist over workdays until done
    member = models.ForeignKey(Member, related_name="goals", on_delete=models.CASCADE)
    desc = models.CharField(max_length=200)
    status = models.CharField(max_length=45)
    added = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField()

class Scorecard(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    daily_avg = models.IntegerField() # daily assignments
    weekly_avg = models.IntegerField() # weekly assignments
    time_vs_est = models.IntegerField() # percentage
    # more calculations via logic on views.py (this week, last week)