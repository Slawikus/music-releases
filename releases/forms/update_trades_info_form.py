from django import forms
from django.forms import ModelForm

from releases.models import ReleaseTradesInfo


class UpdateReleaseTradesInfoForm(ModelForm):
    class Meta:
        model = ReleaseTradesInfo
        exclude = ['release']
        widgets = {
            'available_for_trade': forms.RadioSelect,
        }
