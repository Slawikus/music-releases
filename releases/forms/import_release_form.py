from django import forms


class ImportReleaseForm(forms.Form):

    file = forms.FileField(
        widget=forms.FileInput(attrs={"accept": ".csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel"})
    )