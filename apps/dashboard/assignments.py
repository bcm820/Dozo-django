
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Import models from Django
from django.db import models
from models import Assignment

# Import time ops
from datetime import timedelta



# Python Fundamentals 1
def pyfun1(user):

    Assignment.objects.create(
        user=user, track='pyfun1', pageid='pyfun101',
        title = "Strings and Lists", base_points = 1,
        est_duration=timedelta(hours=1), time_mult = 2)

    Assignment.objects.create(
        user=user, track='pyfun1', pageid='pyfun102',
        title = "Multiply, Sum, Average", base_points = 1,
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
def pyfun2(user):

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
        est_duration=timedelta(hours=2), time_mult = 3)

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
def pyoop(user):

    Assignment.objects.create(
        user=user, track='pyoop', pageid='pyoop1',
        title = "Bike", base_points = 2,
        est_duration=timedelta(hours=2), time_mult = 3)

    Assignment.objects.create(
        user=user, track='pyoop', pageid='pyoop2',
        title = "Car", base_points = 2,
        est_duration=timedelta(hours=2), time_mult = 3)

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
        est_duration=timedelta(hours=2), time_mult = 3)

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
        est_duration=timedelta(hours=2), time_mult = 3)

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
        est_duration=timedelta(hours=2), time_mult = 3)

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
        est_duration=timedelta(hours=2), time_mult = 3)

    Assignment.objects.create(
        user=user, track='mysql', pageid='mysql2',
        title = "Blogs", base_points = 2,
        est_duration=timedelta(hours=2), time_mult = 3)

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
        est_duration=timedelta(hours=2), time_mult = 3)

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



# Flask & MySQL
def flask2(user):

    Assignment.objects.create(
        user=user, track='flask2', pageid='flask201',
        title = "Connection Errors", base_points = 1,
        est_duration=timedelta(minutes=20), time_mult = 1.33)

    Assignment.objects.create(
        user=user, track='flask2', pageid='flask202',
        title = "Full Friends", base_points = 1,
        est_duration=timedelta(hours=2), time_mult = 3)

    Assignment.objects.create(
        user=user, track='flask2', pageid='flask203',
        title = "Email Validation with DB", base_points = 1,
        est_duration=timedelta(hours=2), time_mult = 3)

    Assignment.objects.create(
        user=user, track='flask2', pageid='flask204',
        title = "Login and Registration", base_points = 2,
        est_duration=timedelta(hours=4), time_mult = 3)

    Assignment.objects.create(
        user=user, track='flask2', pageid='flask205',
        title = "The Wall", base_points = 4,
        est_duration=timedelta(hours=8), time_mult = 6)

    Assignment.objects.create(
        user=user, track='flask2', pageid='flask206',
        title = "Users", base_points = 4,
        est_duration=timedelta(hours=4), time_mult = 3)

    # Calculate potential for each assignment
    for assignment in user.assignments.filter(status='a'):
        assignment.potential = assignment.base_points * assignment.time_mult
        assignment.save()



# Django
def django(user):

    Assignment.objects.create(
        user=user, track='django', pageid='django1',
        title = "Django App", base_points = 1,
        est_duration=timedelta(minutes=45), time_mult = 1.75)

    Assignment.objects.create(
        user=user, track='django', pageid='django2',
        title = "Time Display", base_points = 2,
        est_duration=timedelta(hours=2), time_mult = 3)

    Assignment.objects.create(
        user=user, track='django', pageid='django3',
        title = "Random Word Generator", base_points = 1,
        est_duration=timedelta(hours=1), time_mult = 2)

    Assignment.objects.create(
        user=user, track='django', pageid='django4',
        title = "Survey Form", base_points = 2,
        est_duration=timedelta(hours = 3), time_mult = 3)

    Assignment.objects.create(
        user=user, track='django', pageid='django5',
        title = "Session Words", base_points = 3,
        est_duration=timedelta(hours=4), time_mult = 3)

    Assignment.objects.create(
        user=user, track='django', pageid='django6',
        title = "Amadon", base_points = 3,
        est_duration=timedelta(hours=4), time_mult = 3)

    Assignment.objects.create(
        user=user, track='django', pageid='django7',
        title = "Ninja Gold", base_points = 3,
        est_duration=timedelta(hours=3), time_mult = 3)

    Assignment.objects.create(
        user=user, track='django', pageid='django8',
        title = "Multiple Apps", base_points = 2,
        est_duration=timedelta(hours=2), time_mult = 3)

    # Calculate potential for each assignment
    for assignment in user.assignments.filter(status='a'):
        assignment.potential = assignment.base_points * assignment.time_mult
        assignment.save()



# Python: Django ORM
def djangoorm(user):

    Assignment.objects.create(
        user=user, track='djangoorm', pageid='django1',
        title = "Users", base_points = 1,
        est_duration=timedelta(hours=2), time_mult = 3)

    Assignment.objects.create(
        user=user, track='djangoorm', pageid='django2',
        title = "Dojo Ninjas", base_points = 1,
        est_duration=timedelta(hours=2), time_mult = 3)

    Assignment.objects.create(
        user=user, track='djangoorm', pageid='django3',
        title = "Books/Authors", base_points = 2,
        est_duration=timedelta(hours=3), time_mult = 3)

    Assignment.objects.create(
        user=user, track='djangoorm', pageid='django4',
        title = "Likes/Books", base_points = 3,
        est_duration=timedelta(hours=4), time_mult = 4)

    Assignment.objects.create(
        user=user, track='djangoorm', pageid='django5',
        title = "Semi-Restful Users", base_points = 3,
        est_duration=timedelta(hours=3), time_mult = 3)

    Assignment.objects.create(
        user=user, track='djangoorm', pageid='django6',
        title = "Courses", base_points = 3,
        est_duration=timedelta(hours=3), time_mult = 3)

    Assignment.objects.create(
        user=user, track='djangoorm', pageid='django7',
        title = "Login and Registration", base_points = 4,
        est_duration=timedelta(hours=5), time_mult = 5)

    Assignment.objects.create(
        user=user, track='djangoorm', pageid='django8',
        title = "Belt Reviewer", base_points = 3,
        est_duration=timedelta(hours=4), time_mult = 4)

    # Calculate potential for each assignment
    for assignment in user.assignments.filter(status='a'):
        assignment.potential = assignment.base_points * assignment.time_mult
        assignment.save()



# Java Fundamentals
def javafun(user):

    Assignment.objects.create(
        user=user, track='javafun', pageid='javafun1',
        title = "First Java Program", base_points = 1,
        est_duration=timedelta(minutes=30), time_mult = 1.5)

    Assignment.objects.create(
        user=user, track='javafun', pageid='javafun2',
        title = "Pythagorean Theorem", base_points = 1,
        est_duration=timedelta(minutes=30), time_mult = 1.5)

    Assignment.objects.create(
        user=user, track='javafun', pageid='javafun3',
        title = "Fizzbuzz", base_points = 1,
        est_duration=timedelta(minutes=30), time_mult = 1.5)

    Assignment.objects.create(
        user=user, track='javafun', pageid='javafun4',
        title = "String Manipulation", base_points = 2,
        est_duration=timedelta(hours=1), time_mult = 2)

    Assignment.objects.create(
        user=user, track='javafun', pageid='javafun5',
        title = "Basics", base_points = 2,
        est_duration=timedelta(hours=1), time_mult = 2)

    Assignment.objects.create(
        user=user, track='javafun', pageid='javafun6',
        title = "Puzzling", base_points = 2,
        est_duration=timedelta(hours=1), time_mult = 2)

    Assignment.objects.create(
        user=user, track='javafun', pageid='javafun7',
        title = "Map of the Hashmatique", base_points = 1,
        est_duration=timedelta(minutes=30), time_mult = 1.5)

    Assignment.objects.create(
        user=user, track='javafun', pageid='javafun8',
        title = "Exceptions and Generics", base_points = 1,
        est_duration=timedelta(minutes=30), time_mult = 1.5)

    # Calculate potential for each assignment
    for assignment in user.assignments.filter(status='a'):
        assignment.potential = assignment.base_points * assignment.time_mult
        assignment.save()



# Java OOP
def javaoop(user):

    Assignment.objects.create(
        user=user, track='javaoop', pageid='javaoop1',
        title = "Project Class", base_points = 1,
        est_duration=timedelta(minutes=30), time_mult = 1.5)

    Assignment.objects.create(
        user=user, track='javaoop', pageid='javaoop2',
        title = "Singly Linked List", base_points = 2,
        est_duration=timedelta(hours=1), time_mult = 2)

    Assignment.objects.create(
        user=user, track='javaoop', pageid='javaoop3',
        title = "Zoo Keeper 1", base_points = 1,
        est_duration=timedelta(minutes=30), time_mult = 1.5)

    Assignment.objects.create(
        user=user, track='javaoop', pageid='javaoop4',
        title = "Zoo Keeper 2", base_points = 1,
        est_duration=timedelta(minutes=30), time_mult = 1.5)

    Assignment.objects.create(
        user=user, track='javaoop', pageid='javaoop5',
        title = "Object Master 1", base_points = 2,
        est_duration=timedelta(hours=1), time_mult = 2)

    Assignment.objects.create(
        user=user, track='javaoop', pageid='javaoop6',
        title = "Object Master 2", base_points = 2,
        est_duration=timedelta(hours=1), time_mult = 2)

    Assignment.objects.create(
        user=user, track='javaoop', pageid='javaoop7',
        title = "Bank Account", base_points = 2,
        est_duration=timedelta(hours=1), time_mult = 2)

    Assignment.objects.create(
        user=user, track='javaoop', pageid='javaoop8',
        title = "Pokemon", base_points = 2,
        est_duration=timedelta(hours=1), time_mult = 2)

    Assignment.objects.create(
        user=user, track='javaoop', pageid='javaoop9',
        title = "Calculator 1", base_points = 2,
        est_duration=timedelta(hours=1), time_mult = 2)

    # Calculate potential for each assignment
    for assignment in user.assignments.filter(status='a'):
        assignment.potential = assignment.base_points * assignment.time_mult
        assignment.save()



# Java Spring
def javaspring1(user):

    Assignment.objects.create(
        user=user, track='javaspring1', pageid='javaspring101',
        title = "Strings", base_points = 1,
        est_duration=timedelta(hours=1), time_mult = 2)

    Assignment.objects.create(
        user=user, track='javaspring1', pageid='javaspring102',
        title = "Portfolio", base_points = 1,
        est_duration=timedelta(hours=1), time_mult = 2)

    Assignment.objects.create(
        user=user, track='javaspring1', pageid='javaspring103',
        title = "Display Date", base_points = 1,
        est_duration=timedelta(hours=1), time_mult = 2)

    Assignment.objects.create(
        user=user, track='javaspring1', pageid='javaspring104',
        title = "Display Date", base_points = 1,
        est_duration=timedelta(hours=1), time_mult = 2)

    Assignment.objects.create(
        user=user, track='javaspring1', pageid='javaspring105',
        title = "Display Date", base_points = 1,
        est_duration=timedelta(hours=1), time_mult = 2)

    Assignment.objects.create(
        user=user, track='javaspring1', pageid='javaspring106',
        title = "Hello Human", base_points = 1,
        est_duration=timedelta(hours=1), time_mult = 2)

    Assignment.objects.create(
        user=user, track='javaspring1', pageid='javaspring107',
        title = "Dojo Survey", base_points = 2,
        est_duration=timedelta(hours=1), time_mult = 2)

    Assignment.objects.create(
        user=user, track='javaspring1', pageid='javaspring108',
        title = "Ninja Gold Game", base_points = 3,
        est_duration=timedelta(hours=3), time_mult = 4)

    Assignment.objects.create(
        user=user, track='javaspring1', pageid='javaspring109',
        title = "Learning Platform", base_points = 4,
        est_duration=timedelta(hours=3), time_mult = 4)

    Assignment.objects.create(
        user=user, track='javaspring1', pageid='javaspring110',
        title = "The Code", base_points = 1,
        est_duration=timedelta(minutes=30), time_mult = 1.5)

    # Calculate potential for each assignment
    for assignment in user.assignments.filter(status='a'):
        assignment.potential = assignment.base_points * assignment.time_mult
        assignment.save()



# Java Spring Data
def javaspringdata(user):

    Assignment.objects.create(
        user=user, track='javaspringdata', pageid='javaspringdata1',
        title = "Group Languages", base_points = 2,
        est_duration=timedelta(hours=2), time_mult = 3)

    Assignment.objects.create(
        user=user, track='javaspringdata', pageid='javaspringdata2',
        title = "Languages, Reloaded", base_points = 2,
        est_duration=timedelta(hours=2), time_mult = 3)

    Assignment.objects.create(
        user=user, track='javaspringdata', pageid='javaspringdata3',
        title = "Lookify", base_points = 4,
        est_duration=timedelta(hours=3), time_mult = 4)

    Assignment.objects.create(
        user=user, track='javaspringdata', pageid='javaspringdata4',
        title = "Lookify", base_points = 4,
        est_duration=timedelta(hours=3), time_mult = 4)

    Assignment.objects.create(
        user=user, track='javaspringdata', pageid='javaspringdata5',
        title = "Driver's License", base_points = 3,
        est_duration=timedelta(hours=1), time_mult = 2)

    Assignment.objects.create(
        user=user, track='javaspringdata', pageid='javaspringdata6',
        title = "Dojo and Ninjas", base_points = 3,
        est_duration=timedelta(hours=1), time_mult = 2)

    Assignment.objects.create(
        user=user, track='javaspringdata', pageid='javaspringdata7',
        title = "Products and Categories", base_points = 3,
        est_duration=timedelta(hours=1), time_mult = 2)

    Assignment.objects.create(
        user=user, track='javaspringdata', pageid='javaspringdata8',
        title = "DojoOverflow", base_points = 4,
        est_duration=timedelta(hours=4), time_mult = 4)

    # Calculate potential for each assignment
    for assignment in user.assignments.filter(status='a'):
        assignment.potential = assignment.base_points * assignment.time_mult
        assignment.save()



# Java Spring
def javaspring2(user):

    Assignment.objects.create(
        user=user, track='javaspring2', pageid='javaspring201',
        title = "Countries (JPA Version)", base_points = 3,
        est_duration=timedelta(hours=2), time_mult = 3)

    Assignment.objects.create(
        user=user, track='javaspring2', pageid='javaspring202',
        title = "Employees and Managers", base_points = 3,
        est_duration=timedelta(minutes=30), time_mult = 3)

    Assignment.objects.create(
        user=user, track='javaspring2', pageid='javaspring203',
        title = "Pagination and Sorting", base_points = 3,
        est_duration=timedelta(minutes=30), time_mult = 3)

    Assignment.objects.create(
        user=user, track='javaspring2', pageid='javaspring204',
        title = "Login and Registration", base_points = 3,
        est_duration=timedelta(hours=2), time_mult = 3)

    Assignment.objects.create(
        user=user, track='javaspring2', pageid='javaspring205',
        title = "Admin Dashboard", base_points = 4,
        est_duration=timedelta(hours=3), time_mult = 4)

    Assignment.objects.create(
        user=user, track='javaspring2', pageid='javaspring206',
        title = "Product Catalog", base_points = 3,
        est_duration=timedelta(hours=2), time_mult = 3)

    Assignment.objects.create(
        user=user, track='javaspring2', pageid='javaspring207',
        title = "Product Catalog 2", base_points = 3,
        est_duration=timedelta(hours=2), time_mult = 3)

    Assignment.objects.create(
        user=user, track='javaspring2', pageid='javaspring208',
        title = "Product Catalog 3", base_points = 3,
        est_duration=timedelta(hours=2), time_mult = 3)

    Assignment.objects.create(
        user=user, track='javaspring2', pageid='javaspring209',
        title = "Events", base_points = 4,
        est_duration=timedelta(hours=4), time_mult = 4)

    Assignment.objects.create(
        user=user, track='javaspring2', pageid='javaspring210',
        title = "WaterBnB", base_points = 4,
        est_duration=timedelta(hours=4), time_mult = 4)

    # Calculate potential for each assignment
    for assignment in user.assignments.filter(status='a'):
        assignment.potential = assignment.base_points * assignment.time_mult
        assignment.save()