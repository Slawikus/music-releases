from django.test import TestCase, Client
from users.factories import UserWithProfileFactory
from releases.factories import ReleaseFactory
from django.urls import reverse


class SearchReleaseViewTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = UserWithProfileFactory()
		self.client.force_login(self.user)

	def test_it_finds_release(self):
		ReleaseFactory.create_batch(3)
		ReleaseFactory.create(band_name="Quintino", is_submitted=True)

		response = self.client.post(reverse("search"), {
			"q": "Quint"
		})

		self.assertEqual(response.context['releases'].count(), 1)
		self.assertEqual(response.context['releases'][0].band_name, "Quintino")
