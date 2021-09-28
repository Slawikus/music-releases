from django.views.generic import ListView
from releases.models.release import Release
from itertools import chain
from django.urls import reverse

class SearchListView(ListView):
	template_name = "release/release_list.html"
	context_object_name = "releases"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		url = reverse("search", args=['q'])[:-1]
		context['search_url'] = url
		return context

	def get_queryset(self):
		data = self.request.POST
		by_band_name = Release.objects.filter(band_name__icontains=self.kwargs['q'])
		by_album_title = Release.objects.filter(album_title__icontains=self.kwargs['q'])
		by_label_name = Release.objects.filter(label__name__icontains=self.kwargs['q'])
		by_country = Release.objects.filter(country__icontains=self.kwargs['q'])
		result_list = list(chain(by_band_name, by_album_title, by_label_name, by_country))

		return result_list
