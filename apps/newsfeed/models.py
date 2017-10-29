# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..landing.models import User

from datetime import timedelta


class Scorecard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_score = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    total_assignments = models.IntegerField()
    total_sessions = models.IntegerField()
    total_sessions_ontime = models.IntegerField()
    total_duration = models.DurationField(default=timedelta())
    avg_session_score = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    most_assignments = models.IntegerField()
    avg_assignments_per = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    avg_assignments_ontime = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    avg_duration = models.DurationField(default=timedelta())


class Event(models.Model):

    TYPE = (
        ('s_start', 'Started Session'), # say how many assignments, point potential
        ('a_finish', 'Finished Assignment'), # say which, whether on time, how many pts
        ('s_end', 'Finished Session'), # whether on time, how many points
    )

    user = models.ForeignKey(User, related_name="events", on_delete=models.CASCADE)
    type = models.CharField(max_length=45, choices=TYPE)
    desc = models.TextField()
    added = models.DateTimeField(auto_now_add=True)

