from django import forms
from django.forms import ModelForm

from .models import Release, Label


class DateInput(forms.DateInput):
    input_type = 'date'


class CreateReleaseForm(ModelForm):
    class Meta:
        model = Release
        fields = [
            'band_name',
            'country',
            'album_title',
            'release_date',
            'label',
            'base_style',
            'cover_image',
            'format',
            'sample',
            'media_format_details',
            'limited_edition',
        ]
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
