from django.test import TestCase, Client
from users.factories import LabelFactory, UserWithProfileFactory
from django.urls import reverse
from users.models import Label


class DeleteLabelViewTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = UserWithProfileFactory()
		self.client.force_login(self.user)

	def test_it_delete_not_main_label(self):
		label = LabelFactory.create(profile=self.user.profile)
		self.client.post(reverse('label_delete', args=[label.id]))
		self.assertEqual(Label.objects.count(), 0)

	def test_it_does_not_delete_main_label(self):
		label = LabelFactory.create(profile=self.user.profile)
		label.is_main = True
		label.save()
		self.client.post(reverse('label_delete', args=[label.id]))
		label.refresh_from_db()
		self.assertTrue(Label.objects.filter(name=label.name).exists())
