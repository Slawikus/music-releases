from django.forms import ModelForm
from users.models import Profile


class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['country', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].widget.attrs['rows'] = 5
