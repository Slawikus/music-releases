from django.forms import ModelForm
from users.models import Label


class LabelForm(ModelForm):
    class Meta:
        model = Label
        fields = ['name', 'logo', 'description']

    def __init__(self, *args, **kwargs):
        super(LabelForm, self).__init__(*args, **kwargs)
        self.fields['logo'].widget.attrs.update({'class': 'form-control'})
