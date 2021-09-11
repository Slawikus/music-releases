from django import forms
from django.forms import ModelForm

from releases.models import ReleaseWholesaleInfo


class UpdateReleaseWholesaleInfoForm(ModelForm):
    class Meta:
        model = ReleaseWholesaleInfo
        exclude = ['release']
        widgets = {
            'available_for_wholesale': forms.RadioSelect,
        }
