from django import forms
from django.contrib.auth import password_validation
from django_countries.data import COUNTRIES
from django.core.validators import ValidationError


class UserProfileCreationForm(forms.Form):
	email = forms.EmailField()
	password1 = forms.CharField(
		label="Password",
		strip=False,
		widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
		help_text=password_validation.password_validators_help_text_html(),
	)
	password2 = forms.CharField(
		label="Password confirmation",
		widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
		strip=False,
		help_text="Enter the same password as before, for verification.",
	)
	label_name = forms.CharField(max_length=250)
	country = forms.ChoiceField(choices=COUNTRIES.items())

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise ValidationError(
				self.error_messages['password_mismatch'],
				code='password_mismatch',
			)
		return password2
