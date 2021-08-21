from django.forms import ModelForm
from .models import BandSubmission

class BandSubmissionForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = BandSubmission