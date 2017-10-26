# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Import models from Django
from django.db import models
from models import Assignment, Goal, Scorecard

# Import time ops
import datetime


# ### Calculations ###

#### CREATE A NEW PAGE...... secret :)
# Depending on where people are, change the Dashboard link on top??? #

### To calc whether assignment completed on time....
### Compare with est_time field in minutes


# Potential points a user can earn based on queue and assignment rank
# Calculate prior to finalizing queue; instantiate scorecard!
def potential_points(user):
    
    # Init temp int and store plans query
    potential_points = 0
    if user.assignments.filter(status='b').count() > 0:
        todays_plans = user.assignments.filter(status='b')
    else:
        todays_plans = user.assignments.filter(status='c')
    
    for assignment in todays_plans:
        temp = assignment.points * assignment.time_mult
        potential_points += temp
    
    # Multiply potential points by count of queue
    potential_points *= todays_plans.count()
    
    # Update scorecard with potential points
    scorecard = user.scorecards.get(date = datetime.date.today())
    scorecard.potential = potential_points
    scorecard.save()


# Actual points a user earned (running amount until last assignment)
# Calculate upon completing an assignment; update scorecard!
def actual_points(user):
    
    # Init temp int and store plans query
    actual_points = 0
    done_lane = user.assignments.filter(status='e')
    
    # Calc points based on assignments done on time
    for assignment in done_lane:
        if assignment.on_time == True:
            temp = assignment.points * assignment.time_mult
            actual_points += temp
        actual_points += assignment.points # add points
    
    # if entire queue completed, multiply by count of queue
    todays_plans = user.assignments.filter(status='c')
    if len(todays_plans) == 0:
        actual_points *= done_land.count()
    
    # Update scorecard with actual points
    scorecard = user.scorecards.get(date = datetime.date.today())
    scorecard.actual = actual_points
    scorecard.save()