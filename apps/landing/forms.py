# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from .models import User


# Join Dozo
class CreateUser(forms.ModelForm):

    # Create password and confirmation fields to check
    reg_password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput, help_text="8 characters minimum")
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput, help_text="Must be an exact match")

    # Custom field labels / help text
    first_name = forms.CharField(help_text="3 characters minimum")
    reg_username = forms.CharField(help_text="3 characters minimum")
    last_name = forms.CharField(required=False, help_text="Optional")
    email = forms.EmailField(help_text="Must be valid format")

    # Set meta of form inputs to be User model
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

    # Check that the two password entries match
    def clean_password2(self):
        reg_password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if reg_password1 and password2 and reg_password1 != password2:
            raise forms.ValidationError("Error: Passwords did not match.")
        return password2

    # Create user with hashed password
    def save(self, commit=True):
        user = super(CreateUser, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
