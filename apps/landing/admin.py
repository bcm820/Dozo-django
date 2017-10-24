# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from models import Member

# Admin form for creating new members. Includes all required fields
class SuperMemberCreationForm(forms.ModelForm):

    # Create password and confirmation fields to check
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, help_text="8 characters min.")
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    last_name = forms.CharField(max_length=45, required=False, help_text="Optional")

    # Set meta of form inputs to be Member model
    class Meta:
        model = Member
        fields = '__all__'

    # Check that the two password entries match
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Your passwords do not match.")
        return password2

    # Save the provided password in hashed format
    def save(self, commit=True):
        member = super(MemberCreationForm, self).save(commit=False)
        member.set_password(self.cleaned_data["password1"])
        if commit:
            member.save()
        return member


# Admin form for updating users.  Replaces pw field with admin pw field.
class SuperMemberChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    # Set meta of form inputs to be Member model
    class Meta:
        model = Member
        fields = '__all__'

    # Return initial value of password
    def clean_password(self):
        return self.initial["password"]


class MemberAdmin(BaseUserAdmin):

    # The forms to add and change user instances
    form = SuperMemberChangeForm
    add_form = SuperMemberCreationForm

    # Displays table of members and fields to filter by
    list_display = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('added', 'is_active')

    # How to display the form when changing a member's info
    fieldsets = (
        (None, {'fields': ('username',)}),
        ('Personal', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    # How to display the form when adding a member
    add_fieldsets = (
        (None, {
            'classes': ('wide',), # sets width of field display
            'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(Member, MemberAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)