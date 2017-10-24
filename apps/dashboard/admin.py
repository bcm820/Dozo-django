# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib import admin
from models import Assignment, Goal, Scorecard

class AssignmentAdmin(admin.ModelAdmin):
    pass

class GoalAdmin(admin.ModelAdmin):
    pass

class ScorecardAdmin(admin.ModelAdmin):
    pass

admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(Scorecard, ScorecardAdmin)