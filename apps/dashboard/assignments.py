
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Import models from Django
from django.db import models
from models import Assignment

# Import time ops
from datetime import timedelta



# Python Fundamentals 1
def py_fun1(user):

    Assignment.objects.create(
        user=user, track='pyfun1', pageid='pyfun101',
        title = "Strings and Lists", base_points = 1,
        est_duration=timedelta(hours=1), time_mult = 2)

    Assignment.objects.create(
        user=user, track='pyfun1', pageid='pyfun102',
        title = "Mult, Sum, Avg", base_points = 1,
        est_duration=timedelta(hours=1), time_mult = 2)

    Assignment.objects.create(
        user=user, track='pyfun1', pageid='pyfun103',
        title = "Filter By Type", base_points = 1,
        est_duration=timedelta(minutes=30), time_mult = 1.5)

    Assignment.objects.create(
        user=user, track='pyfun1', pageid='pyfun104',
        title = "Type List", base_points = 1,
        est_duration=timedelta(minutes=45), time_mult = 1.75)

    Assignment.objects.create(
        user=user, track='pyfun1', pageid='pyfun105',
        title = "Comparing Lists", base_points = 1,
        est_duration=timedelta(minutes=20), time_mult = 1.33)

    Assignment.objects.create(
        user=user, track='pyfun1', pageid='pyfun106',
        title = "Finding Characters", base_points = 1,
        est_duration=timedelta(minutes=45), time_mult = 1.75)

    Assignment.objects.create(
        user=user, track='pyfun1', pageid='pyfun107',
        title = "Checkerboard", base_points = 2,
        est_duration=timedelta(minutes=40), time_mult = 1.67)

    # Calculate potential for each assignment
    for assignment in user.assignments.filter(status='a'):
        assignment.potential = assignment.base_points * assignment.time_mult
        assignment.save()



# Python Fundamentals 2
def py_fun2(user):

    Assignment.objects.create(
        user=user, track='pyfun2', pageid='pyfun201',
        title = "Fun with Functions", base_points = 2,
        est_duration=timedelta(hours=2), time_mult = 3)

    Assignment.objects.create(
        user=user, track='pyfun2', pageid='pyfun202',
        title = "Scores and Grades", base_points = 2,
        est_duration=timedelta(hours=1), time_mult = 2)

    Assignment.objects.create(
        user=user, track='pyfun2', pageid='pyfun203',
        title = "Coin Tosses", base_points = 2,
        est_duration=timedelta(hours=1), time_mult = 2)

    Assignment.objects.create(
        user=user, track='pyfun2', pageid='pyfun204',
        title = "Stars", base_points = 3,
        est_duration=timedelta(hours=3), time_mult = 3)

    Assignment.objects.create(
        user=user, track='pyfun2', pageid='pyfun205',
        title = "Dictionary Basics", base_points = 1,
        est_duration=timedelta(minutes=20), time_mult = 1.33)

    Assignment.objects.create(
        user=user, track='pyfun2', pageid='pyfun206',
        title = "Names", base_points = 3,
        est_duration=timedelta(hours=2), time_mult = 2)

    Assignment.objects.create(
        user=user, track='pyfun2', pageid='pyfun207',
        title = "Making Tuples", base_points = 3,
        est_duration=timedelta(minutes=30), time_mult = 3)

    Assignment.objects.create(
        user=user, track='pyfun2', pageid='pyfun208',
        title = "Lists to Dict", base_points = 3,
        est_duration=timedelta(minutes=30), time_mult = 3)

    # Calculate potential for each assignment
    for assignment in user.assignments.filter(status='a'):
        assignment.potential = assignment.base_points * assignment.time_mult
        assignment.save()



# Python OOP
def py_oop(user):

    Assignment.objects.create(
        user=user, track='pyoop', pageid='pyoop1',
        title = "Bike", base_points = 2,
        est_duration=timedelta(hours=2), time_mult = 3)

    Assignment.objects.create(
        user=user, track='pyoop', pageid='pyoop2',
        title = "Car", base_points = 2,
        est_duration=timedelta(hours=2), time_mult = 2)

    Assignment.objects.create(
        user=user, track='pyoop', pageid='pyoop3',
        title = "Product", base_points = 3,
        est_duration=timedelta(hours=2), time_mult = 3)

    Assignment.objects.create(
        user=user, track='pyoop', pageid='pyoop4',
        title = "Animal", base_points = 3,
        est_duration=timedelta(hours=3), time_mult = 3)

    Assignment.objects.create(
        user=user, track='pyoop', pageid='pyoop5',
        title = "Math Dojo", base_points = 2,
        est_duration=timedelta(hours=2), time_mult = 2)

    Assignment.objects.create(
        user=user, track='pyoop', pageid='pyoop6',
        title = "Call Center", base_points = 3,
        est_duration=timedelta(hours=2), time_mult = 3)

    Assignment.objects.create(
        user=user, track='pyoop', pageid='pyoop7',
        title = "Call Center", base_points = 3,
        est_duration=timedelta(hours=2), time_mult = 3)

    Assignment.objects.create(
        user=user, track='pyoop', pageid='pyoop8',
        title = "Hospital", base_points = 3,
        est_duration=timedelta(hours=2), time_mult = 3)

    # Calculate potential for each assignment
    for assignment in user.assignments.filter(status='a'):
        assignment.potential = assignment.base_points * assignment.time_mult
        assignment.save()



# Flask Fundamentals
def flask1(user):

    Assignment.objects.create(
        user=user, track='flask1', pageid='flask101',
        title = "Hello World", base_points = 1,
        est_duration=timedelta(minutes=30), time_mult = 1.5)

    Assignment.objects.create(
        user=user, track='flask1', pageid='flask102',
        title = "Portfolio", base_points = 2,
        est_duration=timedelta(hours=1), time_mult = 2)

    Assignment.objects.create(
        user=user, track='flask1', pageid='flask103',
        title = "Landing Page", base_points = 2,
        est_duration=timedelta(hours=2), time_mult = 2)

    Assignment.objects.create(
        user=user, track='flask1', pageid='flask104',
        title = "What's My Name?", base_points = 1,
        est_duration=timedelta(minutes=20), time_mult = 1.5)

    Assignment.objects.create(
        user=user, track='flask1', pageid='flask105',
        title = "Dojo Survey", base_points = 2,
        est_duration=timedelta(hours=2), time_mult = 3)

    Assignment.objects.create(
        user=user, track='flask1', pageid='flask106',
        title = "Disappearing Ninja", base_points = 2,
        est_duration=timedelta(hours=2), time_mult = 3)

    Assignment.objects.create(
        user=user, track='flask1', pageid='flask107',
        title = "Counter", base_points = 2,
        est_duration=timedelta(hours=2), time_mult = 2)

    Assignment.objects.create(
        user=user, track='flask1', pageid='flask108',
        title = "Great Number Game", base_points = 3,
        est_duration=timedelta(hours=4), time_mult = 4)

    Assignment.objects.create(
        user=user, track='flask1', pageid='flask109',
        title = "Ninja Gold", base_points = 3,
        est_duration=timedelta(hours=4), time_mult = 3)

    Assignment.objects.create(
        user=user, track='flask1', pageid='flask110',
        title = "Dojo Survey with Validation", base_points = 3,
        est_duration=timedelta(hours=4), time_mult = 3)

    Assignment.objects.create(
        user=user, track='flask1', pageid='flask111',
        title = "Registration Form", base_points = 3,
        est_duration=timedelta(hours=4), time_mult = 3)

    # Calculate potential for each assignment
    for assignment in user.assignments.filter(status='a'):
        assignment.potential = assignment.base_points * assignment.time_mult
        assignment.save()



# Flask Fundamentals
def mysql(user):

    Assignment.objects.create(
        user=user, track='mysql', pageid='mysql1',
        title = "Books", base_points = 1,
        est_duration=timedelta(hours=2), time_mult = 2)

    Assignment.objects.create(
        user=user, track='mysql', pageid='mysql2',
        title = "Blogs", base_points = 2,
        est_duration=timedelta(hours=2), time_mult = 2)

    Assignment.objects.create(
        user=user, track='mysql', pageid='mysql3',
        title = "User Dashboard", base_points = 3,
        est_duration=timedelta(hours=3), time_mult = 3)

    Assignment.objects.create(
        user=user, track='mysql', pageid='mysql4',
        title = "Workbench Setup", base_points = 1,
        est_duration=timedelta(minutes=45), time_mult = 1.75)

    Assignment.objects.create(
        user=user, track='mysql', pageid='mysql5',
        title = "Countries", base_points = 1,
        est_duration=timedelta(hours=2), time_mult = 2)

    Assignment.objects.create(
        user=user, track='mysql', pageid='mysql6',
        title = "Sakila", base_points = 2,
        est_duration=timedelta(hours=4), time_mult = 3)

    Assignment.objects.create(
        user=user, track='mysql', pageid='mysql7',
        title = "Friendships", base_points = 4,
        est_duration=timedelta(hours=4), time_mult = 4)

    Assignment.objects.create(
        user=user, track='mysql', pageid='mysql8',
        title = "Lead Gen Business", base_points = 4,
        est_duration=timedelta(hours=4), time_mult = 4)

    # Calculate potential for each assignment
    for assignment in user.assignments.filter(status='a'):
        assignment.potential = assignment.base_points * assignment.time_mult
        assignment.save()



# Python: Django ORM
def py_django_orm(user):

    Assignment.objects.create(
        user=user, track='django', pageid='django1',
        title = "Users", base_points = 1,
        est_duration=timedelta(hours=2), time_mult = 2.5)

    Assignment.objects.create(
        user=user, track='django', pageid='django2',
        title = "Dojo Ninjas", base_points = 1,
        est_duration=timedelta(hours=2), time_mult = 2.5)

    Assignment.objects.create(
        user=user, track='django', pageid='django3',
        title = "Books/Authors", base_points = 2,
        est_duration=timedelta(hours=3), time_mult = 3)

    Assignment.objects.create(
        user=user, track='django', pageid='django4',
        title = "Likes/Books", base_points = 3,
        est_duration=timedelta(hours=4), time_mult = 4)

    Assignment.objects.create(
        user=user, track='django', pageid='django5',
        title = "Semi-Restful Users", base_points = 3,
        est_duration=timedelta(hours=3), time_mult = 3)

    Assignment.objects.create(
        user=user, track='django', pageid='django6',
        title = "Courses", base_points = 3,
        est_duration=timedelta(hours=3), time_mult = 3)

    Assignment.objects.create(
        user=user, track='django', pageid='django7',
        title = "Login and Registration", base_points = 4,
        est_duration=timedelta(hours=5), time_mult = 5)

    Assignment.objects.create(
        user=user, track='django', pageid='django8',
        title = "Belt Reviewer", base_points = 3,
        est_duration=timedelta(hours=4), time_mult = 4)

    # Calculate potential for each assignment
    for assignment in user.assignments.filter(status='a'):
        assignment.potential = assignment.base_points * assignment.time_mult
        assignment.save()