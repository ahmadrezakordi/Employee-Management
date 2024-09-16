from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    job = forms.ModelChoiceField(queryset=Job.objects.all(), initial=0)

    class Meta:
        model = Employee
        fields = '__all__'

