from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    prefix = 'profile'

    class Meta(UserCreationForm):
        model = User
        fields = ['email']