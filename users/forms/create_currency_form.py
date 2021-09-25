from django import forms
from django.forms import ModelForm

from configuration.settings import CURRENCY_CHOICES
from users.models import ProfileCurrency


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
        profile_currencies = ProfileCurrency.objects.filter(profile=profile).values_list('currency', flat=True)
        currency_choices = [choice for choice in CURRENCY_CHOICES
                            if choice[0] not in profile_currencies]

        return currency_choices
