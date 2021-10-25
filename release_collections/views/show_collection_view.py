from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from release_collections.models import ReleaseCollection
from releases.models import Release



class ShowCollectionView(LoginRequiredMixin, ListView):
	context_object_name = "releases"
	template_name = "release/release_list.html"
	model = Release

	def get_queryset(self):
		collection = ReleaseCollection.objects.get(pk=self.kwargs['pk'])
		releases = []
		for release_id in collection.release_ids:
			releases.append(get_object_or_404(Release, pk=release_id))

		return releases
