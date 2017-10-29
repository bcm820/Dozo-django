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
from ..landing.models import User
from models import Assignment, Session
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
    
    # if not archived assignments, redirect to dash2
    if request.user.assignments.filter(status='e').count() > 0:
        return redirect(reverse('dashboard:dozo'))
    
    context = {
        'online_users': User.objects.filter(is_online=True),
        'user_assignments': len(request.user.assignments.filter(status='e')|request.user.assignments.filter(status='f')),
        'user_sessions': request.user.sessions.all().count(),
        'assignments': request.user.assignments.filter(status='a'),
        'plans': request.user.assignments.filter(status='b'),
        'commit': request.user.assignments.filter(status='c'),
        'current': request.user.assignments.filter(status='d'),
        'done': request.user.assignments.filter(status='e').order_by("-id")
    }

    # run function to calculate total potential points
    if request.user.assignments.filter(status='b').count() > 0:
        potential = potential_points(request.user)
        context['potential'] = potential
    elif request.user.assignments.filter(status='c').count() > 0:
        potential = potential_points(request.user)
        context['potential'] = potential
    else:
        context['potential'] = 0

    # run function to calculate total est_duration and time challenge
    if request.user.assignments.filter(status='b').count() > 0:
        duration, bonus, challenge = time_challenge(request.user)
        context['duration'] = duration
        context['bonus'] = bonus
        context['challenge'] = challenge
    elif request.user.assignments.filter(status='c').count() > 0:
        duration, bonus, challenge = time_challenge(request.user)
        context['duration'] = duration
        context['bonus'] = bonus
        context['challenge'] = challenge
    else:
        context['duration'] = timedelta()
        context['bonus'] = timedelta()
        context['challenge'] = timedelta()

    return render(request, 'dashboard/dash.html', context)



# Add Assignments
@require_POST
def assignments(request):

    if request.POST['track'] == 'pyfun1':
        pyfun1(request.user)

    if request.POST['track'] == 'pyfun2':
        pyfun2(request.user)

    if request.POST['track'] == 'pyoop':
        pyoop(request.user)

    if request.POST['track'] == 'flask1':
        flask1(request.user)

    if request.POST['track'] == 'mysql':
        mysql(request.user)

    if request.POST['track'] == 'flask2':
        flask2(request.user)

    if request.POST['track'] == 'django':
        django(request.user)

    if request.POST['track'] == 'djangoorm':
        djangoorm(request.user)

    if request.POST['track'] == 'javafun':
        javafun(request.user)

    if request.POST['track'] == 'javaoop':
        javaoop(request.user)

    if request.POST['track'] == 'javaspring1':
        javaspring1(request.user)

    if request.POST['track'] == 'javaspringdata':
        javaspringdata(request.user)

    if request.POST['track'] == 'javaspring2':
        javaspring2(request.user)

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


# Clear assignments list
def clear(request):
    if request.user.assignments.filter(status='a').count() == 0:
        return redirect(reverse('dashboard:dash'))
    else:
        for assignment in request.user.assignments.filter(status='a'):
            assignment.delete()
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

    # get est_duration and challenge
    duration, bonus, challenge = time_challenge(request.user)
    
    # create scoreboard and add assignments and calcs to it
    Session.objects.create(
        user = request.user, 
        potential = potential_points(request.user), 
        est_duration = duration,
        time_bonus = bonus,
        time_challenge = challenge)
    session = request.user.sessions.last()
    for assignment in request.user.assignments.filter(status='c'):
        session.assignments.add(assignment)
        assignment.save()

    return redirect(reverse('dashboard:dash'))


# Start continuous work queue
def go(request):
    
    # If session start time not recorded, record
    session = request.user.sessions.last()
    if session.start == None:
        session.start = timezone.now()
        session.save()
    
    # query assignments in lanes
    # note: query stored in a variable stores as uniterable object
    commit = request.user.assignments.filter(status='c')
    current = request.user.assignments.filter(status='d')
    done = request.user.assignments.filter(status='e')

    # if all assignments done (after results), redirect to dashboard
    if request.user.assignments.filter(
        status='c').count() == 0 and request.user.assignments.filter(
        status='d').count() == 0:

        return redirect(reverse('dashboard:dash'))

    # if assignment just finished, update to done and log times
    if request.user.assignments.filter(status='d').count() == 1:
        done = request.user.assignments.get(status='d')
        done.status = 'e'
        done.end_time = timezone.now()
        done.act_duration = done.end_time - done.start_time
        if done.act_duration < done.est_duration:
            done.on_time = True # update on_time bool
        done.save()

        # record session end time (update each assignment)
        # update on-time bool
        session.end = timezone.now()
        session.act_duration = session.end - session.start
        if session.act_duration < session.time_challenge:
            session.on_time = True
        session.save()

        # add points to the scorecard for the session
        # calculate final score if session is done
        actual_points(request.user)

    # if assignments in queue, start new assignment
    if request.user.assignments.filter(status='c').count() > 0:
        start_new = request.user.assignments.filter(status='c').first()
        start_new.status='d'
        start_new.start_time = timezone.now()
        start_new.save()

    return redirect(reverse('dashboard:dozo'))


# DOZO
@login_required(login_url='/')
def dozo(request):
    
    context = {
        'all_current': Assignment.objects.filter(status='d'),
        'user_assignments': len(request.user.assignments.filter(status='e')|request.user.assignments.filter(status='f')),
        'user_sessions': request.user.sessions.all().count(),
        'online_users': User.objects.filter(is_online=True),
        'assignments': request.user.assignments.filter(status='a'),
        'commit': request.user.assignments.filter(status='c'),
        'current': request.user.assignments.filter(status='d'),
        'done': request.user.assignments.filter(status='e').order_by("-id"),
        'stats': request.user.assignments.filter(status='e'),
        'session': request.user.sessions.last(),
        'remaining': len(request.user.assignments.filter(status='c')|request.user.assignments.filter(status='d'))
    }

    return render(request, 'dashboard/dash2.html', context)


# Done -> Display
def archive(request):
    
    # move assignment to plans lane by updating status field
    for assignment in Assignment.objects.filter(status='e'):
        assignment.status = 'f'
        assignment.save()

    return redirect(reverse('dashboard:dash'))