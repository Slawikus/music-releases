from django import forms
from public_tradelist.models import TradeRequest
from django.core.validators import ValidationError
import re


class UserTradeListForm(forms.ModelForm):
    items = forms.CharField(max_length=255)
    items.widget = forms.TextInput(attrs={"type": "hidden"})

    class Meta:
        model = TradeRequest
        exclude = '__all__'

    def clean_items(self):
        data = self.cleaned_data["items"]
        if data == "":
            raise ValidationError("No item has been chosen")

        # TODO сделать регулярку мощнее
        if not re.match(r"\d+:\d+", data):
            raise ValidationError("Wrong data format")

        return data
