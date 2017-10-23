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
from models import Member
from forms import CreateMember


# Home
def home(request):
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
        return redirect('/dashboard/')
        
    # Re-render the form with invalid data passed in
    else: # Django will take care of rendering validations!
        form = { "form": CreateMember(request.POST) }
        return render(request, 'members/join.html', form)