# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# All the usuals
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string

# Misc for IFTTT connection
from dozo.settings import SECRET_KEY, IFTTT_KEY

# Models
from ..members.models import Member
from models import Device, Session


# IFTTT
@login_required(login_url='/')
def sync(request):
    return render(request, 'ifttt/sync.html')


# Setup
@login_required(login_url='/')
def generate(request):

    # Create new device and assign ifttt_id to user in session
    Device.objects.create(
        owner = request.user,
        ifttt_id = get_random_string(length=5))

    return redirect(reverse('ifttt:sync'))


# Start Session
def start(request):
    
    # Obtain request keys and app key
    client_key = request.GET.get('key', '')
    app_key = SECRET_KEY

    # If keys are matching, confirm member
    if (client_key == app_key):
        device_id = request.body

        # Check device_id against database
        # (CHECK)

        # Check if connection has been recorded in DB
        # If not, record and post success message on dashboard
        # Still leave the device_id on their page

        # Instantiate new session

        return redirect('/')


# End Session
def end(request):
    
    # Obtain request keys and app key
    client_key = request.GET.get('key', '')
    app_key = SECRET_KEY

    # If keys are matching, confirm member
    if (client_key == app_key):
        device_id = request.body

        # Check device_id against database
        return redirect('/')







