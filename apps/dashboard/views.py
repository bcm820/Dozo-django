# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# All the usuals
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


# Models and forms
from ..landing.models import Member


# Home
@login_required(login_url='/')
def dash(request):

    # Set online status
    if request.user.is_online == False:
        request.user.is_online = True
        request.user.save()

    context = { 'online_users': Member.objects.filter(is_online=1) }

    return render(request, 'dashboard/dash.html', context)