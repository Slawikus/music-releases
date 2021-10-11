import json

from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from releases.models import Release
from playlists.models import Playlist, PlaylistItem



class PlaylistCreateView(LoginRequiredMixin, View):
	def get(self, request):
		releases = Release.submitted.filter(profile=request.user.profile)
		return render(request, "playlist/playlist_create.html", {"releases": releases})

	def post(self, request):
		post_data = request.POST
		playlist = Playlist.objects.create(
			profile=request.user.profile,
			name=post_data['playlist_name']
		)

		data = json.loads(post_data['data'])
		for queue, release_id in data.items():

			release = get_object_or_404(Release, id=release_id)

			PlaylistItem.objects.create(
				playlist=playlist,
				order=queue,
				release=release
			)

		return HttpResponseRedirect(reverse("playlist_list"))
