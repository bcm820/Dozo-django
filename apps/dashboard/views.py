# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# All the usuals
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Models and forms
from ..landing.models import Member
from models import Assignment, Goal, Scorecard
from calculations import *
from assignments import *

# Import time ops
import datetime
from django.utils import timezone


# Home
@login_required(login_url='/')
def dash(request):

    # Set online status upon login
    if request.user.is_online == False:
        request.user.is_online = True
        request.user.save()

    # run function to calculate total potential points
    if request.user.assignments.filter(status='b').count() > 0:
        potential = potential_points(request.user)
    
    context = {
        'online_users': Member.objects.filter(is_online=True),
        'assignments': request.user.assignments.filter(status='a'),
        'plans': request.user.assignments.filter(status='b'),
        'commit': request.user.assignments.filter(status='c'),
        'current': request.user.assignments.filter(status='d'),
        'done': request.user.assignments.filter(status='e').order_by("-id")
        'potential': potential
    }

    return render(request, 'dashboard/dash.html', context)


# Add Assignments
@require_POST
def assignments(request):

    if request.POST['track'] == 'py_fun':
        py_fun(request.user)

    if request.POST['track'] == 'py_django_orm':
        py_django_orm(request.user)

    for assignment in request.user.assignments.filter(status='a'):
        assignment.potential = assignment.base_points * assignment.time_mult

    return redirect(reverse('dashboard:dash'))


# Assignments -> Plans
def addtoplans(request, id):
    
    # if user committed already, don't add assignment to session
    if request.user.assignments.filter(status='c').count() > 0:
        return redirect(reverse('dashboard:dash'))
    
    # if not commited, add assignments to plans
    plan = Assignment.objects.get(id=id)
    plan.status = 'b'
    plan.save()

    return redirect(reverse('dashboard:dash'))


# Assignments <- Plans
def remfromplans(request, id):
    
    # move assignment back to lane
    plan = Assignment.objects.get(id=id)
    plan.status = 'a'
    plan.save()

    return redirect(reverse('dashboard:dash'))


# Commit Plans
def commit(request):
    
    # if no plans to commit, redirect to dashboard!
    if request.user.assignments.filter(status='b').count() == 0:
        return redirect(reverse('dashboard:dash'))
    
    # commit plans by updating status field
    for assignment in request.user.assignments.filter(status='b'):
        assignment.status = 'c'
        assignment.save()
    
    # create scorecard with timestamp to link to assignments
    # store timestamp in session to query scorecard later
    timestamp = timezone.now()
    Scorecard.objects.create(member=request.user, timestamp=timestamp)
    request.session['timestamp'] = timestamp

    # timestamp assignments, add assignments to scorecard, update potential
    scorecard = Scorecard.objects.get(timestamp=timestamp)
    scorecard.potential = potential_points(request.user)
    for assignment in request.user.assignments.filter(status='c'):
        scorecard.assignments.add(assignment)
        assignment.timestamp = timestamp
        assignment.save()

    return redirect(reverse('dashboard:dash'))


# Start continuous work queue
def go(request):
    
    # query assignments in lanes
    # note: query stored in a variable stores as uniterable object
    commit = request.user.assignments.filter(status='c')
    current = request.user.assignments.filter(status='d')
    done = request.user.assignments.filter(status='e')

    # if commit is empty (all assignments done), redirect to dash
    if request.user.assignments.filter(
        status='c').count() == 0 and request.user.assignments.filter(
            status='d').count() == 0:
        return redirect(reverse('dashboard:dash'))

    # if assignment just finished, update to done and log times
    if request.user.assignments.filter(status='d').count() > 0:
        done = request.user.assignments.get(status='d')
        done.status = 'e'
        done.end_time = timezone.now()
        done.act_duration = done.end_time - done.start_time
        if done.act_duration < done.est_duration:
            done.on_time = True # update on_time bool
        done.save()

        # add points to the scorecard for the session
        actual_points(request.user, done)

    
    # if assignments in queue, start new assignment
    if request.user.assignments.filter(status='c').count() > 0:
        for assignment in request.user.assignments.filter(status='c')[0:1]:
            assignment.status = 'd'
            assignment.start_time = timezone.now()
            assignment.save()

    return redirect(reverse('dashboard:dozo'))


# DOZO
@login_required(login_url='/')
def dozo(request):
    
    context = {
        'online_users': Member.objects.filter(is_online=True),
        'assignments': request.user.assignments.filter(status='a'),
        'commit': request.user.assignments.filter(status='c'),
        'current': request.user.assignments.filter(status='d'),
        'done': request.user.assignments.filter(status='e').order_by("-id"),
        'stats': request.user.assignments.filter(status='e'),
        'scorecard': Scorecard.objects.get(timestamp=request.session['timestamp'])
    }

    return render(request, 'dashboard/dash2.html', context)


# Done -> Display
def archive(request):
    
    # move assignment to plans lane by updating status field
    for assignment in Assignment.objects.filter(status='e'):
        assignment.status = 'f'
        assignment.save()

    return redirect(reverse('dashboard:dash'))