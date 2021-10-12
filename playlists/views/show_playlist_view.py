from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from playlists.models import Playlist
from releases.models import Release



class ShowPlaylistView(LoginRequiredMixin, ListView):
	context_object_name = "releases"
	template_name = "release/release_list.html"
	model = Release

	def get_queryset(self):
		playlist = Playlist.objects.get(pk=self.kwargs['pk'])
		releases = []
		for release_id in playlist.release_ids:
			releases.append(get_object_or_404(Release, pk=release_id))

		return releases
