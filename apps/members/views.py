# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from models import Member
from forms import CreateMember

# Index (Home)
def index(request):
    return render(request, 'members/index.html')

# Registration form
def join(request):

    # Render registration form created in forms.py
    form = { "form": CreateMember() }

    return render(request, 'members/join.html', form)

# POST request to join
def register(request):

    if request.method == 'POST':

        # Pass post data into the ModelForm to validate before saving
        form = CreateMember(request.POST)
        if form.is_valid():
            form.save()

            # Get username and password to auto-login
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            # return redirect('/members/success/')
            return redirect('/success/')

        else:
            # Render the form with invalid data passed in
            # Invalid data will cause errors to display too!
            form = { "form": CreateMember(request.POST) }

        return render(request, 'members/join.html', form)

    else:
        # return redirect('/members/join/')
        return redirect(reverse('join'))


# TEMPORARY: I'll use this until I get the app up and running.
@login_required(login_url='/')
def success(request):
    return render(request, 'members/success.html')