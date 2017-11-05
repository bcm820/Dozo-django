# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Scorecard, Event

class ScorecardAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'score',
        'duration',
        'sessions',
        'sessions_ontime',
        'assignments',
        'assignments_ontime',
        'max_assignments'
    )
    list_filter = (
        'user',
    )

    search_fields = ('user',)
    ordering = ('score','duration','sessions','assignments','max_assignments')
    filter_horizontal = ()

class EventAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'type',
        'desc',
        'added'
    )
    list_filter = (
        'user',
    )

    search_fields = ('user',)
    ordering = ('user','added')
    filter_horizontal = ()

admin.site.register(Scorecard, ScorecardAdmin)
admin.site.register(Event, EventAdmin)