from django import forms
from django_countries.data import COUNTRIES
from django.contrib.auth.forms import UserCreationForm
from users.models import User


class SignUpForm(UserCreationForm):
    main_label_name = forms.CharField(
        max_length=250,
        label="Name of your main label",
        help_text="Sub-labels can be added later."
    )
    country = forms.ChoiceField(
        choices=COUNTRIES.items(),
        help_text="Current geographical location of your warehouse."
    )

    class Meta:
        model = User
        fields = ("name", "email")
