from django.forms import ModelForm
from releases.models import ReleaseWholesalePrice


class CreateWholesalePriceForm(ModelForm):
    class Meta:
        model = ReleaseWholesalePrice
        exclude = ['release']

    def __init__(self, release, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['currency'].queryset = release.currencies_without_price()
