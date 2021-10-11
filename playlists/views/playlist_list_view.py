from django.views.generic import ListView
from playlists.models import Playlist


class PlaylistListView(ListView):
	context_object_name = "playlists"
	model = Playlist
	template_name = "playlist/playlist_list.html"
