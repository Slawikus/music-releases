from django import forms
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.forms import ModelForm

from releases.models import Release

class UpdateReleaseForm(ModelForm):
    class Meta:
        model = Release
        fields = ['band_name', 'album_title', 'cover_image', 'sample', 'limited_edition']
        widgets = {
            'sample': forms.FileInput(attrs={'accept': 'application/mp3'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['cover_image'].widget.attrs.update({'class': 'form-control'})
        self.fields['sample'].widget.attrs.update({'class': 'form-control'})

    def clean_cover_image(self):
        cover_image = self.cleaned_data['cover_image']
        width, height = get_image_dimensions(cover_image)

        if width != height:
            raise ValidationError('The uploaded image must be square')
        if width < 800:
            raise ValidationError('The uploaded image should have minimal dimension of 800px')

        return self.cleaned_data["cover_image"]