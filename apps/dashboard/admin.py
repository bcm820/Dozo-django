# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib import admin
from models import Assignment, Goal, Scorecard

class AssignmentAdmin(admin.ModelAdmin):

    list_display = ('title', 'status', 'potential', 'actual')
    list_filter = ('user', 'status')

    # edit info
    # fieldsets = (
    #     (None, {'fields': ('username', 'password')}),
    #     ('Personal', {'fields': ('first_name', 'last_name', 'email')}),
    #     ('Permissions', {'fields': ('is_admin',)}),
    # )

    # add info
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',), # sets width of field display
    #         'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')}
    #     ),
    # )
    # search_fields = ('email',)
    # ordering = ('email',)
    # filter_horizontal = ()

class GoalAdmin(admin.ModelAdmin):
    pass

class ScorecardAdmin(admin.ModelAdmin):
    pass

admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(Scorecard, ScorecardAdmin)