from django.forms import ModelForm
from users.models import Profile


class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['label_name', 'country', 'address']
