from django.views.generic import ListView
from releases.models import FavouriteRelease, Release


class FavouriteReleasesView(ListView):
	model = FavouriteRelease
	context_object_name = 'releases'
	template_name = 'release/release_list.html'

	def get_queryset(self):
		releases = FavouriteRelease.objects.filter(profile=self.request.user.profile)
		result = []
		for pk in releases.values_list('pk', flat=True):
			result.append(Release.objects.get(pk=pk))
		return result
