from django.views.generic import ListView
from playlists.models import Playlist
from releases.models import Release


class ShowPlaylistView(ListView):
	context_object_name = "releases"
	template_name = "release/release_list.html"
	model = Release

	def get_queryset(self):
		playlist = Playlist.objects.get(pk=self.kwargs['pk'])
		items = playlist.items.all().order_by("order")
		release_ids = items.values_list("release", flat=True)
		releases = Release.objects.filter(id__in=release_ids)

		return releases
