# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Import models from Django
from django.db import models
# from ..landing.models import Member
from models import Assignment, Goal, Scorecard



### Generate Assignments ###

# Python Fundamentals
def py_fun(user):

    Assignment.objects.create(
        member = user, pair = user, track = 'a', status = 'a',
        title = "Strings and Lists", points = 1,
        time_est='1 hr.', time_pts = 1)

    Assignment.objects.create(
        member = user, pair = user, track = 'a', status = 'a',
        title = "Multiples, Sum, Average", points = 1,
        time_est='1 hr.', time_pts = 1)

    Assignment.objects.create(
        member = user, pair = user, track = 'a', status = 'a',
        title = "Filter By Type", points = 1,
        time_est='30 min.', time_pts = 0.5)

    Assignment.objects.create(
        member = user, pair = user, track = 'a', status = 'a',
        title = "Type List", points = 1,
        time_est='45 min.', time_pts = 0.75)

    Assignment.objects.create(
        member = user, pair = user, track = 'a', status = 'a',
        title = "Comparing Lists", points = 1,
        time_est='20 min.', time_pts = 0.33)

    Assignment.objects.create(
        member = user, pair = user, track = 'a', status = 'a',
        title = "Finding Characters", points = 1,
        time_est='45 min.', time_pts = 0.75)

    Assignment.objects.create(
        member = user, pair = user, track = 'a', status = 'a',
        title = "Checkerboard", points = 2,
        time_est='40 min.', time_pts = 0.67)

    Assignment.objects.create(
        member = user, pair = user, track = 'a', status = 'a',
        title = "Multiplication Table", points = 2,
        time_est='30 min.', time_pts = 0.5, optional=True)

    Assignment.objects.create(
        member = user, pair = user, track = 'a', status = 'a',
        title = "Foo and Bar", points = 2,
        time_est='1 hr.', time_pts = 1, optional=True)

    Assignment.objects.create(
        member = user, pair = user, track = 'a', status = 'a',
        title = "Turtle", points = 2,
        time_est='1 hr.', time_pts = 1, optional=True)



# ### Calculations ###

# Potential points a user can earn based on queue and assignment rank
# Calculate prior to finalizing queue; instantiate scorecard!
def potential_points(user):
    
    potential_points = 0 # init
    todays_plans = user.assignments.filter(status='b')
    
    for assignment in todays_plans:
        potential_points += assignment.points # add points
        potential_points += assignment.time_pts # add bonus points
    
    potential_points *= todays_plans.count() # multiplier
    
    scorecard = user.scorecards.filter(date = date.today())
    scorecard.potential = potential_points
    scorecard.save()

# Actual points a user earned (running amount until last assignment)
# Calculate upon completing an assignment; update scorecard!
def actual_points(user):
    
    actual_points = 0 # init
    done_lane = user.assignments.filter(status='d')
    
    for assignment in done_lane:
        actual_points += assignment.points # add points
        
        if assignment.on_time == True:
            actual_points += assignment.time_points # bonus pts
    
    todays_plans = user.assignments.filter(status='b')
    if len(todays_plans) == 0:
        actual_points *= done_lane.count() # multiplier
    
    scorecard = user.scorecards.filter(date = date.today())
    scorecard.actual = actual_points
    scorecard.save()
    