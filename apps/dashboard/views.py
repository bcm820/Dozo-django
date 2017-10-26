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

# Import datetime
import datetime


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
        'current': request.user.assignments.filter(status='d'),
        'done': request.user.assignments.filter(status='e')
    }

    # append committed plans to list for queue
    commit_list = []
    for assignment in request.user.assignments.filter(status='c'):
        commit_list.append(assignment)
    context['commit'] = commit_list
    
    # If user's scorecard for today exists, update potential points and add to dict
    if request.user.scorecards.filter(date = datetime.date.today()).count() > 0:
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
    if request.user.scorecards.filter(date = datetime.date.today()).count() == 0:
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