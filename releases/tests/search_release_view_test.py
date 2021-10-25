from django.test import TestCase, Client
from users.factories import UserWithProfileFactory
from releases.factories import ReleaseFactory, SubmittedReleaseFactory
from django.urls import reverse


class SearchReleaseViewTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = UserWithProfileFactory()
		self.client.force_login(self.user)

	def test_it_finds_release(self):
		SubmittedReleaseFactory.create_batch(3)
		SubmittedReleaseFactory.create(band_name="Quintino")

		response = self.client.post(reverse("search"), {
			"q": "Quint"
		})

		self.assertEqual(response.context['releases'].count(), 1)
		self.assertEqual(response.context['releases'][0].band_name, "Quintino")

	def test_it_shows_all_releases_if_q_is_empty(self):
		SubmittedReleaseFactory.create_batch(3)

		response = self.client.post(reverse("search"), {
			"q": ""
		})

		self.assertEqual(response.context['releases'].count(), 3)

	def test_it_redirects_unlogged_user(self):
		client = Client()
		response = client.post(reverse("search"), {
			"q": "Test"
		})

		self.assertEqual(response.status_code, 302)
