from django import forms
from django.forms import ModelForm

from configuration.settings import CURRENCY_CHOICES
from users.models import ProfileCurrency
from .models import Release, Label, WholesaleAndTrades, ReleaseWholesalePrice


class DateInput(forms.DateInput):
    input_type = 'date'


class CreateReleaseForm(ModelForm):
    class Meta:
        model = Release
        exclude = ['profile', 'is_submitted']
        widgets = {
            'release_date': DateInput(),
            'format': forms.RadioSelect,
            'sample': forms.FileInput(attrs={'accept': 'application/mp3'})
        }

    def __init__(self, *args, **kwargs):
        self.profile = kwargs.pop('profile')
        super().__init__(*args, **kwargs)

        self.fields['cover_image'].widget.attrs.update({'class': 'form-control'})
        self.fields['sample'].widget.attrs.update({'class': 'form-control'})

        if self.instance:
            self.fields['label'].queryset = Label.objects.filter(profile=self.profile)


class UpdateTradesAndWholesaleForm(ModelForm):
    class Meta:
        model = WholesaleAndTrades
        exclude = ['release']
        widgets = {
            'available_for_trade': forms.RadioSelect,
            'available_for_wholesale': forms.RadioSelect,
        }


class CreateWholesalePriceForm(ModelForm):
    class Meta:
        model = ReleaseWholesalePrice
        fields = '__all__'
        exclude = ['wholesale_and_trades']

    def __init__(self, profile, wholesale_and_trades, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['profile_currency'].queryset = self.get_currency_choices(profile, wholesale_and_trades)

    @staticmethod
    def get_currency_choices(profile, wholesale_and_trades):
        profile_currencies = ProfileCurrency.objects.filter(profile=profile)
        release_currencies_ids = ReleaseWholesalePrice.objects.filter(wholesale_and_trades=wholesale_and_trades).values_list('profile_currency', flat=True)
        release_currencies = ProfileCurrency.objects.filter(id__in=release_currencies_ids)
        currency_choices = profile_currencies.exclude(id__in=release_currencies)

        return currency_choices
