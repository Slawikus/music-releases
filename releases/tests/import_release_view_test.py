from django.test import TestCase, Client
from users.factories import UserWithProfileFactory
from django.urls import reverse
from configuration.settings import BASE_DIR
from releases.models import Release
from users.factories import LabelFactory


class ImportReleasesViewTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = UserWithProfileFactory()
		self.client.force_login(self.user)

	def test_it_imports_releases(self):
		LabelFactory.create(profile=self.user.profile, name='sandra')
		with open(f"{BASE_DIR}/releases/test_files/example.xlsx", 'rb') as file:
			self.client.post(reverse('import_releases'), {
				'file': file
			})
		# There are 3 releases in example.xlsx file
		self.assertEqual(Release.objects.count(), 3)

	def test_it_does_not_import_if_label_does_not_exist(self):

		with open(f"{BASE_DIR}/releases/test_files/example.xlsx", 'rb') as file:
			self.client.post(reverse('import_releases'), {
				'file': file
			})

		self.assertEqual(Release.objects.count(), 0)
