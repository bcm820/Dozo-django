# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# All the usuals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Models and forms
from models import Member
from forms import CreateMember

# Misc for IFTTT connection
from dozo.settings import SECRET_KEY, IFTTT_KEY
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


# Index (Home)
def index(request):
    return render(request, 'members/index.html')

# Registration form
def join(request):

    # Render registration form created in forms.py
    form = { "form": CreateMember() }
    return render(request, 'members/join.html', form)

@require_POST
def register(request):

    # Pass post data into the ModelForm to validate before saving
    form = CreateMember(request.POST)

    # If valid, save and use post data to auto-login
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return redirect('/success/')
        
    # Re-render the form with invalid data passed in
    else: # Django will take care of rendering validations!
        form = { "form": CreateMember(request.POST) }
        return render(request, 'members/join.html', form)






# TEMPORARY: I'll use this until I get the app up and running.
@login_required(login_url='/')
def success(request):
    return render(request, 'members/success.html')


# TEST ROUTE
def ifttt(request):
    
    # Define keys from request and env var
    client_key = request.GET.get('key', '')
    app_key = SECRET_KEY

    # If key in IFTTT matches app key
    if (client_key == app_key):
        username = request.body



    return HttpResponse('HELLO')