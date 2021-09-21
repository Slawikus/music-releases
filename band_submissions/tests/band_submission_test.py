from django.test import TestCase
from band_submissions.factories import BandSubmissionFactory
from notifications.models import Notification


class BandSubmissionTest(TestCase):
	def test_it_creates_notification(self):

		band_submission = BandSubmissionFactory.create()
		notif_amount = Notification.objects.count()

		self.assertEqual(notif_amount, 1)

		band_submission.biography = "testing biography"
		band_submission.save()

		notif_amount = Notification.objects.count()

		self.assertEqual(notif_amount, 1)
