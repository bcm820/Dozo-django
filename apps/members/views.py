# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from models import Member
from forms import CreateMember

def index(request):
    return render(request, 'index.html')

def join(request):
    form = { "form": CreateMember() }
    return render(request, 'join.html', form)

def register(request):

    if request.method == 'POST':
        bound_form = CreateMember(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            return redirect('/members/success/')
        else:
            form = { "form": CreateMember(request.POST) }
        return render(request, 'join.html', form)
    else:
        return redirect('/members/join/')

def success(request):
    return render(request, 'success.html')