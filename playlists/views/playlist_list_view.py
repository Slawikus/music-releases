from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from playlists.models import Playlist


class PlaylistListView(LoginRequiredMixin, ListView):
	context_object_name = "playlists"
	model = Playlist
	template_name = "playlist/playlist_list.html"
