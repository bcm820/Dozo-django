# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from models import Member
from forms import CreateMember

# Index (Home)
def index(request):
    return render(request, 'members/index.html')

# Registration form
def join(request):
    form = { "form": CreateMember() }
    return render(request, 'members/join.html', form)

# POST request to join
def register(request):
    if request.method == 'POST':
        bound_form = CreateMember(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            # return redirect('/members/success/')
            return redirect(reverse('members:success'))
        else:
            form = { "form": CreateMember(request.POST) }
        return render(request, 'join.html', form)
    else:
        # return redirect('/members/join/')
        return redirect(reverse('members:join'))

# TEMPORARY: I'll use this until I get the app up and running.
def success(request):

    return render(request, 'members/success.html')