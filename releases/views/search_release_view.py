from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from releases.models import Release
from itertools import chain
from django.shortcuts import render
from django.db.models.query_utils import Q


class SearchReleaseView(LoginRequiredMixin, View):

	def post(self, request):
		q = request.POST.get('q')
		releases = Release.submitted.filter(Q(band_name__icontains=q) |
										  Q(album_title__icontains=q) |
										  Q(country__icontains=q) |
										  Q(base_style__icontains=q))

		context = {"releases": releases}

		return render(request, "release/release_list.html", context)
