from django.test import TestCase, Client
from users.factories import LabelFactory, UserWithProfileFactory
from django.urls import reverse
from users.models import ProfileCurrency

class UpdateLabelViewTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = UserWithProfileFactory()
		self.client.force_login(self.user)

	def test_it_updates_label(self):
		label = LabelFactory.create(profile=self.user.profile)
		new_name = 'test label name'
		response = self.client.post(reverse('label_update', args=[label.id]), {
			'name': new_name
		})

		label.refresh_from_db()
		self.assertEqual(label.name, new_name)
