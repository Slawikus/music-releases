from django import forms
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.forms import ModelForm

from releases.models import Release
from users.models import Label

class DateInput(forms.DateInput):
    input_type = 'date'


class CreateReleaseForm(ModelForm):
    class Meta:
        model = Release
        exclude = ['profile', 'is_submitted', 'submitted_at']
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

    def clean_cover_image(self):
        cover_image = self.cleaned_data['cover_image']
        if cover_image is None:
            return self.cleaned_data['cover_image']
        width, height = get_image_dimensions(cover_image)

        if width != height:
            raise ValidationError('The uploaded image must be square')
        if width < 800:
            raise ValidationError('The uploaded image should have minimal dimension of 800px')

        return self.cleaned_data["cover_image"]
