from django.test import TestCase, Client
from band_submissions.factories import BandSubmissionFactory
from users.factories import UserWithProfileFactory
from notifications.models import Notification


class BandSubmissionModelTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = UserWithProfileFactory()
		self.client.force_login(self.user)

	def test_it_creates_notification(self):
		BandSubmissionFactory.create_batch(3, profile=self.user.profile)
		BandSubmissionFactory.create_batch(2)
		notif_amount = Notification.objects.filter(profile=self.user.profile).count()

		self.assertEqual(notif_amount, 3)