# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Import models from Django
from django.db import models
from ..landing.models import Member


# Models: Assignment, Goal, Scorecard 

class Assignment(models.Model):
    TRACKS = (
        ('a', 'Python Fundamentals'),
        ('b', 'Python OOP'),
        ('c', 'Python: Flask'),
    )
    LANE = (
        ('a', 'assignments'),
        ('b', 'plans'),
        ('c', 'current'),
        ('d', 'done'),
        ('e', 'display')
    )
    member = models.ForeignKey(Member, related_name="assignments", on_delete=models.CASCADE)
    pair = models.ForeignKey(Member, related_name="pair_assignment")
    track = models.CharField(max_length=45, choices=TRACKS)
    status = models.CharField(max_length=45, choices=LANE)
    title = models.CharField(max_length=45)
    points = models.IntegerField()
    time_est = models.CharField(max_length=45)
    time_pts = models.DecimalField(max_digits=3, decimal_places=1)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True)
    on_time = models.BooleanField(blank=True) # if on time, add
    optional = models.BooleanField(default=False)

class Goal(models.Model): # goals persist over workdays until done
    member = models.ForeignKey(Member, related_name="goals", on_delete=models.CASCADE)
    desc = models.CharField(max_length=200)
    status = models.CharField(max_length=45)
    added = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField()

class Scorecard(models.Model):
    member = models.ForeignKey(Member, related_name="scorecards", on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, unique=True)
    potential = models.DecimalField(max_digits=4, decimal_places=2)
    actual = models.DecimalField(max_digits=4, decimal_places=2)
    # use scorecards to calculate running total, and find average





# instantiate new scorecard at beginning of QUEUE!!


# Link to ID to move between queues
# Add points color to distinguish!!!

# points
# basic - 1
# intermediate - 2

### Prior to clicking the commit button, clicking the assignments moves them back
### After clicking the commit button, the first assignment in the QUEUE gets bumped into CURRENT. That's the only one you get to click... and when you do, it goes to done and then the NEXT assignment automatically bumps to CURRENT.

# CONTINUOUS WORK!!!



# CURRENTLY WORKING:
# - show list of others working on same assignment, encourage pair programming
# - show assignment page for people to discuss on there....

# Show list of others working on same assignment?!??
# when assignment added to current, show other names who are working on same assignment. ask if you want to work together... they will get option to confirm. then you are paired. in addition to individually working on something.