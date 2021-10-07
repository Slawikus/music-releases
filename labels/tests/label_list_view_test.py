from django.test import TestCase, Client
from django.urls import reverse
from users.factories import UserWithProfileFactory
from labels.factories import LabelFactory

class LabelListViewTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = UserWithProfileFactory()
		self.client.force_login(self.user)

	def test_it_shows_labels(self):
		LabelFactory.create_batch(3)
		response = self.client.get(reverse("label_list"))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['object_list'].count(), 3)

	def test_it_redirects_unlogged_user(self):
		client = Client()
		response = client.get(reverse("label_list"))
		self.assertEqual(response.status_code, 302)
