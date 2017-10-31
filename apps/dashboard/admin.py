# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib import admin
from models import Assignment, Session

class AssignmentAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'user',
        'end_time',
        'act_duration',
        'session',
        'on_time'
    )
    list_filter = (
        'user',
        'status',
        'track',
        'on_time'
    )

    search_fields = ('user',)
    ordering = ('status',)
    filter_horizontal = ()

class SessionAdmin(admin.ModelAdmin):

    list_display = (
        'start',
        'end',
        'user',
        'act_duration',
        'on_time'
    )
    list_filter = (
        'user',
        'on_time'
    )

    search_fields = ('user',)
    ordering = ('act_duration',)
    filter_horizontal = ()

admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Session, SessionAdmin)