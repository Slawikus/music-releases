from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from release_collections.models import ReleaseCollection


class CollectionListView(LoginRequiredMixin, ListView):
	context_object_name = "collections"
	model = ReleaseCollection
	template_name = "collection/collection_list.html"
