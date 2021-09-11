from django import forms
from django.forms import ModelForm

from releases.models import WholesaleAndTrades

class UpdateTradesAndWholesaleForm(ModelForm):
    class Meta:
        model = WholesaleAndTrades
        exclude = ['release']
        widgets = {
            'available_for_trade': forms.RadioSelect,
            'available_for_wholesale': forms.RadioSelect,
        }