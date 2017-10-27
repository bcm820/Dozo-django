
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Import models from Django
from django.db import models
from models import Assignment

# Import time ops
from datetime import timedelta


# Python Fundamentals
def py_fun(user):
    
    Assignment.objects.create(
        member = user, track = 'a', status = 'a',
        title = "1. Strings and Lists", base_points = 1,
        act_duration=timedelta(hours=0),
        est_duration=timedelta(hours=1), time_mult = 2)

    Assignment.objects.create(
        member = user, track = 'a', status = 'a',
        title = "2. Multiples, Sum, Average", base_points = 1,
        act_duration=timedelta(hours=0),
        est_duration=timedelta(hours=1), time_mult = 2)

    Assignment.objects.create(
        member = user, track = 'a', status = 'a',
        title = "3. Filter By Type", base_points = 1,
        act_duration=timedelta(hours=0),
        est_duration=timedelta(minutes=30), time_mult = 1.5)

    Assignment.objects.create(
        member = user, track = 'a', status = 'a',
        title = "4. Type List", base_points = 1,
        act_duration=timedelta(hours=0),
        est_duration=timedelta(minutes=45), time_mult = 1.75)

    Assignment.objects.create(
        member = user, track = 'a', status = 'a',
        title = "5. Comparing Lists", base_points = 1,
        act_duration=timedelta(hours=0),
        est_duration=timedelta(minutes=20), time_mult = 1.33)

    Assignment.objects.create(
        member = user, track = 'a', status = 'a',
        title = "6. Finding Characters", base_points = 1,
        act_duration=timedelta(hours=0),
        est_duration=timedelta(minutes=45), time_mult = 1.75)

    Assignment.objects.create(
        member = user, track = 'a', status = 'a',
        title = "7. Checkerboard", base_points = 2,
        act_duration=timedelta(hours=0),
        est_duration=timedelta(minutes=40), time_mult = 1.67)

    Assignment.objects.create(
        member = user, track = 'a', status = 'a',
        title = "8. Multiplication Table", base_points = 2,
        act_duration=timedelta(hours=0),
        est_duration=timedelta(minutes=30), time_mult = 1.5, optional=True)

    Assignment.objects.create(
        member = user, track = 'a', status = 'a',
        title = "9. Foo and Bar", base_points = 2,
        act_duration=timedelta(hours=0),
        est_duration=timedelta(hours=1), time_mult = 2, optional=True)

    Assignment.objects.create(
        member = user, track = 'a', status = 'a',
        title = "10. Turtle", base_points = 2,
        act_duration=timedelta(hours=0),
        est_duration=timedelta(hours=1), time_mult = 2, optional=True)


# Python: Django ORM
def py_django_orm(user):

    Assignment.objects.create(
        member = user, track = 'b', status = 'a',
        title = "1. Users", base_points = 1,
        act_duration=timedelta(hours=0),
        est_duration=timedelta(hours=2), time_mult = 2.5)

    Assignment.objects.create(
        member = user, track = 'b', status = 'a',
        title = "2. Dojo Ninjas", base_points = 1,
        act_duration=timedelta(hours=0),
        est_duration=timedelta(hours=2), time_mult = 2.5)

    Assignment.objects.create(
        member = user, track = 'b', status = 'a',
        title = "3. Books/Authors", base_points = 2,
        act_duration=timedelta(hours=0),
        est_duration=timedelta(hours=3), time_mult = 3)

    Assignment.objects.create(
        member = user, track = 'b', status = 'a',
        title = "4. Likes/Books", base_points = 3,
        act_duration=timedelta(hours=0),
        est_duration=timedelta(hours=4), time_mult = 4)

    Assignment.objects.create(
        member = user, track = 'b', status = 'a',
        title = "5. Sports ORM", base_points = 3,
        act_duration=timedelta(hours=0),
        est_duration=timedelta(hours=3), time_mult = 3, optional=True)

    Assignment.objects.create(
        member = user, track = 'b', status = 'a',
        title = "6. Sports ORM II", base_points = 3,
        act_duration=timedelta(hours=0),
        est_duration=timedelta(hours=3), time_mult = 3, optional=True)

    Assignment.objects.create(
        member = user, track = 'b', status = 'a',
        title = "7. Semi-Restful Users", base_points = 3,
        act_duration=timedelta(hours=0),
        est_duration=timedelta(hours=3), time_mult = 3)

    Assignment.objects.create(
        member = user, track = 'b', status = 'a',
        title = "8. Courses", base_points = 3,
        act_duration=timedelta(hours=0),
        est_duration=timedelta(hours=3), time_mult = 3)

    Assignment.objects.create(
        member = user, track = 'b', status = 'a',
        title = "9. Login and Registration", base_points = 4,
        act_duration=timedelta(hours=0),
        est_duration=timedelta(hours=5), time_mult = 5)

    Assignment.objects.create(
        member = user, track = 'b', status = 'a',
        title = "10. Belt Reviewer", base_points = 3,
        act_duration=timedelta(hours=0),
        est_duration=timedelta(hours=4), time_mult = 4)