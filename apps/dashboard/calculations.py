# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Import models from Django
from django.db import models
from models import Assignment, Session
from ..newsfeed.models import Scorecard

# Import time ops
from datetime import timedelta


# Calculate total potential points
def potential_points(user):

    # Init container to store potential points
    potential = 0

    # Get assignments in planning or commit lane and add up points
    if user.assignments.filter(status='b').count() > 0:
        plans = user.assignments.filter(status='b')
    elif user.assignments.filter(status='c').count() > 0:
        plans = user.assignments.filter(status='c')
    for assignment in plans:
        potential += assignment.potential
    
    # Multiply potential points by count of queue
    potential *= plans.count()

    return potential


# Calculate time challenge and update scorecard
def time_challenge(user):
    
    # Init container to store total duration
    duration = timedelta()
    
    # Get assignments in planning or commit lane and add up est. time
    if user.assignments.filter(status='b').count() > 0:
        plans = user.assignments.filter(status='b')
    elif user.assignments.filter(status='c').count() > 0:
        plans = user.assignments.filter(status='c')
    for assignment in plans:
        duration += assignment.est_duration
    
    # Add bonus time 
    mult = plans.count() * 0.15
    bonus = timedelta(seconds=mult * duration.total_seconds())
    challenge = timedelta(seconds=bonus.total_seconds() + duration.total_seconds())

    # Return added est_duration, bonus, and time challenge
    return duration, bonus, challenge


# Calculate and add points earned for an assignment to scorecard
def actual_points(user):
    
    # Init container and store 'done' assignments and scorecard
    actual_points = 0
    done_lane = user.assignments.filter(status='e')
    
    # Calc and store points based on assignments done on time
    for assignment in done_lane:
        if assignment.on_time == True:
            assignment.actual = assignment.base_points * assignment.time_mult
            actual_points += assignment.actual
        else:
            assignment.actual = assignment.base_points
            actual_points += assignment.base_points
        assignment.save()
    
    # if session completed under 8 hours, apply queue multiplier
    queue = user.assignments.filter(status='c')
    if len(queue) == 0:
        actual_points *= done_lane.count()
    
    # Add points to current scores and save
    session = user.sessions.last()
    session.actual = actual_points
    session.save()



# scorecard totals
def calc_scorecard(user):

    # create scorecard if none found; query user's scorecard
    if Scorecard.objects.filter(user=user).count() == 0:
        Scorecard.objects.create(user=user)
    scorecard = Scorecard.objects.get(user=user)

    # store user's session and assignment data
    sessions = user.sessions.all()
    assignments = user.assignments.filter(status='f')
    s_ontime = sessions.filter(on_time=True)
    a_ontime = user.assignments.filter(status='f', on_time=True)
    
    # update total score, total duration
    # and max assignments in a session
    score = 0
    max = 0
    duration = timedelta()
    for session in sessions:
        score += session.actual
        duration += session.act_duration
        if session.assignments.count() > max:
            max = session.assignments.count()
    scorecard.score = score
    scorecard.duration = duration
    scorecard.max_assignments = max

    # update total sessions and assignments
    scorecard.assignments = assignments.count()
    scorecard.sessions = sessions.count()

    # update total sessions and assignments on time
    scorecard.sessions_ontime = s_ontime.count()
    scorecard.assignments_ontime = a_ontime.count()

    # save
    scorecard.save()
