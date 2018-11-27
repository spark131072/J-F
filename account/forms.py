"""
131072
221118 - initial
account/forms.py



"""


# =============

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models



class SignUpForm(UserCreationForm):
    YEARS= [x for x in range(1936,2026)]
    GENDER_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female'),
        )


    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(label='Birth Date', widget=forms.SelectDateWidget(years=YEARS))
    gender = forms.ChoiceField(choices = GENDER_CHOICES, required=True, help_text='if you are Male please type \"M\", if you are female please type \"F\".')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'gender', 'birth_date', 'email', 'password1', 'password2')
