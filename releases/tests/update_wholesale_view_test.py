from django.test import TestCase, Client
from users.factories import UserWithProfileFactory
from django.urls import reverse
from releases.factories import ReleaseFactory


class UpdateWholesaleInfoViewTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = UserWithProfileFactory()
		self.client.force_login(self.user)

	def test_it_updates_wholesale(self):
		release = ReleaseFactory.create(profile=self.user.profile)
		response = self.client.post(reverse('release_wholesale_info_edit', args=[release.id]), {
			'available_for_wholesale': True
		})
		release.refresh_from_db()

		self.assertTrue(release.releasewholesaleinfo.available_for_wholesale)
