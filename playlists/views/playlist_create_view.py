import json

from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse

from releases.models import Release
from playlists.models import Playlist



class PlaylistCreateView(LoginRequiredMixin, View):
	def get(self, request):
		releases = Release.submitted.filter(profile=request.user.profile)
		return render(request, "playlist/playlist_create.html", {"releases": releases})

	def post(self, request):
		post_data = request.POST
		release_ids = json.loads(post_data['release_ids'])["all"]

		Playlist.objects.create(
			profile=request.user.profile,
			name=post_data['playlist_name'],
			release_ids=release_ids
		)


		return HttpResponseRedirect(reverse("playlist_list"))
