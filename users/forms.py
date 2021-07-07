from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelForm

from configuration.settings import CURRENCY_CHOICES
from .models import User, Profile, ProfileCurrency


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


class CreateCurrencyForm(ModelForm):
    currency = forms.ModelChoiceField(queryset=ProfileCurrency.objects.none())

    class Meta:
        model = ProfileCurrency
        fields = ['currency']

    def __init__(self, profile, *args, **kwargs):
        super(CreateCurrencyForm, self).__init__(*args, **kwargs)
        self.fields['currency'].choices = self.get_currency_choices(profile)

    @staticmethod
    def get_currency_choices(profile):
        profile_currencies = list(ProfileCurrency.objects.filter(profile=profile).values())
        profile_currencies_names = []

        for currency in profile_currencies:
            for key, value in currency.items():
                if key == 'currency':
                    profile_currencies_names.append(value)

        currency_choices = [choice for choice in CURRENCY_CHOICES
                            if choice[0] not in profile_currencies_names]

        return currency_choices
