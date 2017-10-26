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
from dashboard import *
from assignments import *

# Import time ops
import datetime
from django.utils import timezone
from dateutil.relativedelta import relativedelta


# Home
@login_required(login_url='/')
def dash(request):

    # Set online status upon login
    if request.user.is_online == False:
        request.user.is_online = True
        request.user.save()

    context = {
        'online_users': Member.objects.filter(is_online=True),
        'assignments': request.user.assignments.filter(status='a'),
        'plans': request.user.assignments.filter(status='b'),
        'commit': request.user.assignments.filter(status='c'),
        'current': request.user.assignments.filter(status='d'),
        'done': request.user.assignments.filter(status='e').order_by("-id")
    }
    
    # If user's scorecard for today exists, update potential points and add to dict
    if request.user.scorecards.filter(date = datetime.date.today()).count() > 0:
        if not request.user.assignments.filter(status='d').count() > 0:
            points = potential_points(request.user)
        context['potential_points'] = request.user.scorecards.get(
            date = datetime.date.today()).potential

    return render(request, 'dashboard/dash.html', context)


# Add Assignments
@require_POST
def assignments(request):

    if request.POST['track'] == 'py_fun':
        py_fun(request.user)

    if request.POST['track'] == 'py_django_orm':
        py_django_orm(request.user)

    return redirect(reverse('dashboard:dash'))


# Assignments -> Plans
def addtoplans(request, id):
    
    # if user committed already, redirect back to dashboard!
    if request.user.assignments.filter(status='c').count() > 0:
        return redirect(reverse('dashboard:dash'))
    
    # if start of queue (no scorecard today), create scorecard
    if request.user.scorecards.filter(
        date = datetime.date.today()).count() == 0:
        Scorecard.objects.create(
            member = request.user,
            date = datetime.date.today()
        )
    
    # move assignment to plans lane by updating status field
    plan = Assignment.objects.get(id=id)
    plan.status = 'b'
    plan.save()

    return redirect(reverse('dashboard:dash'))


# Assignments <- Plans
def remfromplans(request, id):
    
    # move assignment back to lane by updating status field
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

    return redirect(reverse('dashboard:dash'))


# Start continuous work queue
def go(request):
    
    # query assignments in lanes
    # note: query stored in a variable stores as uniterable object
    commit = request.user.assignments.filter(status='c'),
    current = request.user.assignments.filter(status='d'),
    done = request.user.assignments.filter(status='e')

    # if commit is empty (all assignments done), redirect to dash
    if request.user.assignments.filter(status='c').count() == 0:
        return redirect(reverse('dashboard:dash'))

    # if assignment just finished, update to done and log times
    if request.user.assignments.filter(status='d').count() > 0:
        done = request.user.assignments.get(status='d')
        done.status = 'e'
        done.end_time = timezone.now()
        done.act_duration = done.end_time - done.start_time

        # update on_time status
        if done.act_duration < done.est_duration:
            done.on_time = True

        # add points to scorecard and save assignment updates
        actual_points(request.user)
        done.save()
    
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
        'done': request.user.assignments.filter(status='e').order_by("-id")
    }
    
    # If user's scorecard for today exists, update potential points and add to dict
    if request.user.scorecards.filter(date = datetime.date.today()).count() > 0:
        if not request.user.assignments.filter(status='d').count() > 0:
            points = potential_points(request.user)
        context['potential_points'] = request.user.scorecards.get(
            date = datetime.date.today()).potential

    return render(request, 'dashboard/dash2.html', context)


# Done -> Display
def archive(request, id):
    
    # move assignment to plans lane by updating status field
    archive = Assignment.objects.get(id=id)
    archive.status = 'f'
    archive.save()

    return redirect(reverse('dashboard:dash'))