from django.views.generic import View
from releases.models import FavouriteRelease
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from releases.models import Release
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect


class CreateFavouriteReleaseView(LoginRequiredMixin, View):
	http_method_names = ['post']

	def post(self, request, pk):
		release = get_object_or_404(Release, pk=pk)
		FavouriteRelease.objects.create(profile=request.user.profile, release=release)
		return HttpResponseRedirect(reverse_lazy('all_releases'))
