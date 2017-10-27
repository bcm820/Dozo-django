# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Import models from Django
from django.db import models
from models import Assignment, Goal, Scorecard

# Import time ops
import datetime


# Calculate total potential points
def potential_points(user):

    # Init container to store potential points
    potential_points = 0

    # Get assignments in planning or commit lane and add points
    if request.user.assignments.filter(status='b').count() > 0:
        plans = request.user.assignments.filter(status='b')
    elif request.user.assignments.filter(status='c').count() > 0:
        plans = request.user.assignments.filter(status='c')
    for assignment in plans:
        potential_points += assignment.potential
    
    # Multiply potential points by count of queue
    potential_points *= plans.count()

    return potential_points


# Calculate and add points earned for an assignment to scorecard
def actual_points(user, assignment):
    
    # Init container and store 'done' assignments and scorecard
    actual_points = 0
    done_lane = user.assignments.filter(status='e')
    
    # Calc points based on assignments done on time
    for assignment in done_lane:
        if assignment.on_time == True:
            temp = assignment.points * assignment.time_mult
            actual_points += temp
        else:
            actual_points += assignment.points # add up points
    
    # if entire queue completed, apply queue multiplier
    queue = user.assignments.filter(status='c')
    if len(queue) == 0:
        actual_points *= done_lane.count()    
    
    # Add points to day's current scores and save
    scorecard = user.scorecards.get(assignments = assignment)
    scorecard.actual += actual_points
    scorecard.save()