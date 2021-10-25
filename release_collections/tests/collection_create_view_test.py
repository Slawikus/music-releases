import json

from django.test import TestCase, Client
from django.urls import reverse

from releases.factories import SubmittedReleaseFactory
from users.factories import UserWithProfileFactory
from release_collections.models import ReleaseCollection


class CollectionCreateViewTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = UserWithProfileFactory()
		self.client.force_login(self.user)

	def test_it_creates_collection(self):
		release1 = SubmittedReleaseFactory.create(profile=self.user.profile)
		release2 = SubmittedReleaseFactory.create(profile=self.user.profile)

		release_ids = [release1.id, release2.id]
		name = "top 2021 best music"

		release_ids_json = json.dumps({"all": release_ids})

		response = self.client.post(reverse("collection_create"), {
			"release_ids": release_ids_json,
			"collection_name": name,

		})

		self.assertEqual(response.status_code, 302)
		self.assertTrue(ReleaseCollection.objects.filter(name=name).exists())

		collection = ReleaseCollection.objects.get(name=name)

		self.assertEqual(collection.release_ids, release_ids)

	def test_it_redirects_unlogged_user(self):
		client = Client()
		response = client.get(reverse("collection_create"))

		self.assertRedirects(response, expected_url=f"{reverse('login')}?next={reverse('collection_create')}")


