from django.forms import ModelForm
from band_submissions.models import BandSubmission


class BandSubmissionForm(ModelForm):
    class Meta:
        exclude = ['profile']
        model = BandSubmission
