from django.test import TestCase, Client
from django.urls import reverse

from releases.factories import ReleaseFactory
from users.factories import UserWithProfileFactory
from playlists.models import Playlist



class ShowPlaylistViewTest(TestCase):
	def setUp(self):
		self.user = UserWithProfileFactory()
		self.client = Client()
		self.client.force_login(self.user)

	def test_it_shows_playlist(self):
		release1 = ReleaseFactory.create(is_submitted=True)
		release2 = ReleaseFactory.create(is_submitted=True)

		playlist = Playlist.objects.create(
			profile=self.user.profile,
			name='test profile',
			release_ids=[release1.id, release2.id]
		)

		response = self.client.get(reverse("playlist_show", args=[playlist.id]))
		release_amount_in_response = len(response.context["releases"])

		self.assertEqual(release_amount_in_response, 2)

	def test_it_redirects_unlogged_user(self):
		client = Client()
		playlist = Playlist.objects.create(
			profile=self.user.profile,
			name='test profile',
			release_ids=[]
		)

		response = client.get(reverse("playlist_show", args=[playlist.id]))

		self.assertRedirects(response, expected_url=f"{reverse('login')}?next={reverse('playlist_show', args=[playlist.id])}")
