# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..landing.models import User

from datetime import timedelta


class Scorecard(models.Model):
    user = models.OneToOneField(User, related_name="scorecard", on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    duration = models.DurationField(default=timedelta())
    sessions = models.IntegerField(default=0)
    assignments = models.IntegerField(default=0)
    sessions_ontime = models.IntegerField(default=0)
    assignments_ontime = models.IntegerField(default=0)
    max_assignments = models.IntegerField(default=0)
    # most assignments finished in a session


class Event(models.Model):

    TYPE = (
        ('s_start', 'Started Session'), # assignment amt, point potential
        ('a_finish', 'Finished Assignment'), # title, on time, pts earned
        ('s_end', 'Finished Session'), # whether on time, pts total
    )

    user = models.ForeignKey(User, related_name="events", on_delete=models.CASCADE)
    type = models.CharField(max_length=45, choices=TYPE)
    desc = models.TextField()
    added = models.DateTimeField(auto_now_add=True)

