# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError


# Validators
# See forms.py for password confirmation validator
def lenLessThanFive(value):
    if len(value) < 5:
        raise ValidationError('(!)')

def lenLessThanEight(value):
    if len(value) < 8:
        raise ValidationError('(!)')


class MemberManager(BaseUserManager):

    def create_user(self, username, first_name, email, password = None):
        
        member = self.model(
            username = username,
            first_name = first_name,
            email = self.normalize_email(email)
        )
        member.set_password(password)
        member.save(using = self._db)
        return member

    def create_superuser(self, username, first_name, email, password = None):
        member = self.create_user(
            username,
            first_name,
            email,
            password=password
        )
        member.is_admin = True
        member.save(using = self._db)
        return member


class Member(AbstractBaseUser):
    first_name = models.CharField(max_length=45, validators=[lenLessThanFive])
    last_name = models.CharField(max_length=45)
    username = models.CharField(max_length=45, unique=True, validators=[lenLessThanFive])
    email = models.EmailField(max_length=45, unique=True)
    password = models.CharField(max_length=100, validators=[lenLessThanEight])
    added = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MemberManager()

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