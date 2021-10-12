import json

from django.test import TestCase, Client
from django.urls import reverse

from releases.factories import ReleaseFactory
from users.factories import UserWithProfileFactory
from playlists.models import Playlist


class PlaylistCreateViewTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = UserWithProfileFactory()
		self.client.force_login(self.user)

	def test_it_creates_playlist(self):
		release1 = ReleaseFactory.create(profile=self.user.profile)
		release2 = ReleaseFactory.create(profile=self.user.profile)

		release_ids = [release1.id, release2.id]
		name = "top 2021 best music"

		release_ids_json = json.dumps({"all": release_ids})

		response = self.client.post(reverse("playlist_create"), {
			"release_ids": release_ids_json,
			"playlist_name": name,

		})

		self.assertEqual(response.status_code, 302)
		self.assertTrue(Playlist.objects.filter(name=name).exists())

		playlist = Playlist.objects.get(name=name)

		self.assertEqual(playlist.release_ids, release_ids)

	def test_it_redirects_unlogged_user(self):
		client = Client()
		response = client.get(reverse("playlist_create"))

		self.assertEqual(response.status_code, 302)


