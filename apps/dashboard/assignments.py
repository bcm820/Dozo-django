
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Import models from Django
from django.db import models
from models import Assignment



# Python Fundamentals
def py_fun(user):
    
    # Create objects
    
    Assignment.objects.create(
        member = user, pair = user, track = 'a', status = 'a',
        title = "1. Strings and Lists", points = 1,
        est_time=60, time_est='1 hr.', time_mult = 2)

    Assignment.objects.create(
        member = user, pair = user, track = 'a', status = 'a',
        title = "2. Multiples, Sum, Average", points = 1,
        est_time=60, time_est='1 hr.', time_mult = 2)

    Assignment.objects.create(
        member = user, pair = user, track = 'a', status = 'a',
        title = "3. Filter By Type", points = 1,
        est_time=30, time_est='30 min.', time_mult = 1.5)

    Assignment.objects.create(
        member = user, pair = user, track = 'a', status = 'a',
        title = "4. Type List", points = 1,
        est_time=45, time_est='45 min.', time_mult = 1.75)

    Assignment.objects.create(
        member = user, pair = user, track = 'a', status = 'a',
        title = "5. Comparing Lists", points = 1,
        est_time=20, time_est='20 min.', time_mult = 1.33)

    Assignment.objects.create(
        member = user, pair = user, track = 'a', status = 'a',
        title = "6. Finding Characters", points = 1,
        est_time=45, time_est='45 min.', time_mult = 1.75)

    Assignment.objects.create(
        member = user, pair = user, track = 'a', status = 'a',
        title = "7. Checkerboard", points = 2,
        est_time=40, time_est='40 min.', time_mult = 1.67)

    Assignment.objects.create(
        member = user, pair = user, track = 'a', status = 'a',
        title = "8. Multiplication Table", points = 2,
        est_time=30, time_est='30 min.', time_mult = 1.5, optional=True)

    Assignment.objects.create(
        member = user, pair = user, track = 'a', status = 'a',
        title = "9. Foo and Bar", points = 2,
        est_time=60, time_est='1 hr.', time_mult = 2, optional=True)

    Assignment.objects.create(
        member = user, pair = user, track = 'a', status = 'a',
        title = "10. Turtle", points = 2,
        est_time=60, time_est='1 hr.', time_mult = 2, optional=True)


# Python: Django ORM
def py_django_orm(user):

    Assignment.objects.create(
        member = user, pair = user, track = 'b', status = 'a',
        title = "1. Users", points = 1,
        est_time=180, time_est='2 hrs.', time_mult = 2.5)

    Assignment.objects.create(
        member = user, pair = user, track = 'b', status = 'a',
        title = "2. Dojo Ninjas", points = 1,
        est_time=180, time_est='2 hrs.', time_mult = 2.5)

    Assignment.objects.create(
        member = user, pair = user, track = 'b', status = 'a',
        title = "3. Books/Authors", points = 2,
        est_time=180, time_est='3 hrs.', time_mult = 3)

    Assignment.objects.create(
        member = user, pair = user, track = 'b', status = 'a',
        title = "4. Likes/Books", points = 3,
        est_time=240, time_est='4 hrs.', time_mult = 4)

    Assignment.objects.create(
        member = user, pair = user, track = 'b', status = 'a',
        title = "5. Sports ORM", points = 3,
        est_time=180, time_est='3 hrs.', time_mult = 3, optional=True)

    Assignment.objects.create(
        member = user, pair = user, track = 'b', status = 'a',
        title = "6. Sports ORM II", points = 3,
        est_time=180, time_est='3 hrs.', time_mult = 3, optional=True)

    Assignment.objects.create(
        member = user, pair = user, track = 'b', status = 'a',
        title = "7. Semi-Restful Users", points = 3,
        est_time=180, time_est='3 hrs.', time_mult = 3)

    Assignment.objects.create(
        member = user, pair = user, track = 'b', status = 'a',
        title = "8. Courses", points = 3,
        est_time=180, time_est='3 hrs.', time_mult = 3)

    Assignment.objects.create(
        member = user, pair = user, track = 'b', status = 'a',
        title = "9. Login and Registration", points = 4,
        est_time=300, time_est='5 hrs.', time_mult = 5)

    Assignment.objects.create(
        member = user, pair = user, track = 'b', status = 'a',
        title = "10. Belt Reviewer", points = 3,
        est_time=240, time_est='4 hrs.', time_mult = 4)