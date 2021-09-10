from django.forms import ModelForm
from releases.models import MarketingInfos


class UpdateMarketingInfosForm(ModelForm):
    class Meta:
        model = MarketingInfos
        exclude = ['release']
