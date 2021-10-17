from django import forms
from playlists.models import Playlist


class PlaylistCreateForm(forms.ModelForm):

	class Meta:
		model = Playlist
		fields = ["name", "label"]
		widgets = {
			'label': forms.RadioSelect
		}