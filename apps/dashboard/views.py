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


# Home
@login_required(login_url='/')
def dash(request):

    # Set online status upon login
    if request.user.is_online == False:
        request.user.is_online = True
        request.user.save()

    # Calculate potential points from today's queue
    # call potential_points function

    context = {
        'online_users': Member.objects.filter(is_online=True),
        'assignments': request.user.assignments.filter(status='a'),
        'plans': request.user.assignments.filter(status='b'),
        'current': request.user.assignments.filter(status='c'),
        'done': request.user.assignments.filter(status='d'),
        'potential_points': potential_points
    }

    return render(request, 'dashboard/dash.html', context)


# Assignments
@require_POST
def assignments(request):

    if request.POST['track'] == 'py_fun':
        pyFun(request.user)

    return redirect(reverse('dashboard:dash'))
