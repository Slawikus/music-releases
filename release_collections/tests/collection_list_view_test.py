from django.test import TestCase, Client
from django.urls import reverse

from users.factories import UserWithProfileFactory
from release_collections.models import ReleaseCollection

class CollectionListViewTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = UserWithProfileFactory()
		self.client.force_login(self.user)

	def test_it_shows_collections_list(self):
		ReleaseCollection.objects.create(profile=self.user.profile, name='test1', release_ids=[])
		ReleaseCollection.objects.create(profile=self.user.profile, name='test2', release_ids=[])

		response = self.client.get(reverse("collection_list"))
		collections_amount_in_response = response.context['object_list'].count()

		self.assertEqual(collections_amount_in_response, 2)

	def test_it_redirects_unlogged_user(self):
		client = Client()
		response = client.get(reverse("collection_list"))

		self.assertRedirects(response, expected_url=f"{reverse('login')}?next={reverse('collection_list')}")
