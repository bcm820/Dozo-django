# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Import models from Django
from django.db import models
from ..members.models import Member


# Create Device Model
class Device(models.Model):
    owner = models.ForeignKey(Member, related_name="owner") # 1-to-1
    ifttt_id = models.CharField(max_length=8)
    connected = models.BooleanField(default=False) # whether connected to IFTTT
    in_session = models.BooleanField() # whether currently logging hours


# Create Session Model
class Session(models.Model): # instantiated at arrival
    member = models.ForeignKey(Member, related_name="workday")
    calendar_date = models.DateTimeField()
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField() # added at departure
    duration = models.IntegerField() # calculated (timedelta) after departure