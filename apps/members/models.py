# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MemberManager(BaseUserManager):

    def create_member(self, first_name, username, email, password = None):
        if not email:
            raise ValueError('You must provide an email address.')

        member = self.model(
            first_name = first_name,
            username = username,
            email = self.normalize_email(email)
        )
        member.set_password(password)
        member.save(using = self._db)
        return member

    def create_admin(self, username, first_name, last_name, email, password = None):
        member = self.create_member(
            first_name,
            username,
            email,
            password=password
        )
        member.is_admin = True
        member.save(using = self._db)
        return member


class Member(AbstractBaseUser):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45, help_text="Optional")
    username = models.CharField(max_length=45, unique=True)
    email = models.EmailField(max_length=45, unique=True)
    password = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    objects = MemberManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'email', 'password']

    def get_full_name(self):
        return self.first_name, self.last_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.username

    def has_perm(self, perm, objec=None):
        "Does the member have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the member have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the member on staff?"
        return self.is_admin

    # Returns url to access an instance of the model.
    def get_absolute_url(self):
        return reverse('view', args=[str(self.id)])