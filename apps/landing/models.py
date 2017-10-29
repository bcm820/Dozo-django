# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Import models and validations from Django
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError

# 
from django.core.cache import cache 
import datetime
from dozo import settings


# Create custom validators
# See forms.py for password confirmation validator
def lenLessThanThree(value):
    if len(value) < 3:
        raise ValidationError('This field requires 3 characters minimum.')

def lenLessThanEight(value):
    if len(value) < 8:
        raise ValidationError('Your password must be 8 characters minimum.')


# Manager for user creation
class UserManager(BaseUserManager):

    def create_user(self, username, first_name, email, password = None):
        user = self.model(
            username = username,
            first_name = first_name,
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, username, first_name, email, password = None):
        user = self.create_user(
            username,
            first_name,
            email,
            password=password
        )
        user.is_admin = True
        user.save(using = self._db)
        return user


# Create user Model (replaces Django's auth.Model)
class User(AbstractBaseUser):
    
    STACKS = (
        ('webfun', 'Web Fundamentals'),
        ('python', 'Python'),
        ('java', 'Java'),
        ('mean', 'MEAN')
    )
    
    first_name = models.CharField(max_length=45, validators=[lenLessThanThree])
    last_name = models.CharField(max_length=45)
    username = models.CharField(max_length=45, unique=True, validators=[lenLessThanThree])
    email = models.EmailField(max_length=45, unique=True)
    password = models.CharField(max_length=100, validators=[lenLessThanEight])
    added = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)
    is_familiar = models.BooleanField(default=False)
    current_stack = models.CharField(max_length=45, choices=STACKS)

    # Instantiate userManager object
    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'email']

    def get_full_name(self):
        return self.first_name, self.last_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.username

    def has_perm(self, perm, objec=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin