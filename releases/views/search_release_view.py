from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from releases.models import Release
from itertools import chain
from django.shortcuts import render


class SearchReleaseView(LoginRequiredMixin, View):

	def post(self, request):
		q = request.POST.get('q')
		rel = Release.objects.filter(band_name__icontains=q)
		rel2 = Release.objects.filter(album_title__icontains=q)
		rel3 = Release.objects.filter(base_style__icontains=q)
		rel4 = Release.objects.filter(country__icontains=q)
		result = list(chain(rel, rel2, rel3, rel4))

		context = {"releases": result}

		return render(request, "release/release_list.html", context)
