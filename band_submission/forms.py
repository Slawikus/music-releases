from django.forms import ModelForm
from .models import BandSubmission


class BandSubmissionForm(ModelForm):
    class Meta:
        exclude = ['profile']
        model = BandSubmission
