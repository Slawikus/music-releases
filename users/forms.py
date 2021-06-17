from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelForm

from .models import User, Profile


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm):
        model = User
        fields = ['email']


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = User
        fields = ['email', 'password']


class EditProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['label_name', 'country', 'address']
