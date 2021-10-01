from django import forms
from django_countries.data import COUNTRIES
from django.contrib.auth.forms import UserCreationForm
from users.models import User


class SignUpForm(UserCreationForm):
	label_name = forms.CharField(max_length=250)
	country = forms.ChoiceField(choices=COUNTRIES.items())

	class Meta:
		model = User
		fields = ("username", "email")
