# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from .models import Member


# Join Dozo
class CreateMember(forms.ModelForm):

    # Create password and confirmation fields to check
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput, help_text="8 characters minimum")
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput, help_text="Must be an exact match for verification")

    # Custom field labels / help text
    first_name = forms.CharField(help_text="3 characters minimum")
    username = forms.CharField(help_text="3 characters minimum")
    last_name = forms.CharField(required=False, help_text="(Optional)")
    email = forms.EmailField(help_text="Must be valid format")

    # Set meta of form inputs to be Member model
    class Meta:
        model = Member
        fields = ('first_name', 'last_name', 'username', 'email')

    # Check that the two password entries match
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Your passwords are not matching.")
        return password2

    # Create user with hashed password
    def save(self, commit=True):
        member = super(CreateMember, self).save(commit=False)
        member.set_password(self.cleaned_data["password1"])
        if commit:
            member.save()
        return member
