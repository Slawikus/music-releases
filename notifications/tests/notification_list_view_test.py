from django.test import TestCase, Client
from users.factories import UserWithProfileFactory
from public_tradelist.factories import TradeRequestFactory
from  band_submissions.factories import BandSubmissionFactory
from notifications.models import Notification
from django.urls import reverse


class NotificationListViewTest(TestCase):
	def setUp(self):
		self.user = UserWithProfileFactory.create()
		self.client = Client()
		self.client.force_login(self.user)

	def test_it_creates_notifications(self):
		TradeRequestFactory.create_batch(2)
		BandSubmissionFactory.create_batch(2)

		self.assertEqual(Notification.objects.count(), 4)

	def test_it_shows_notifications(self):
		TradeRequestFactory.create_batch(3, profile=self.user.profile)
		BandSubmissionFactory.create_batch(2, profile=self.user.profile)

		response = self.client.get(reverse("notifications"))
		notif_amount = response.context["object_list"].count()

		self.assertEqual(notif_amount, 5)

	def test_it_does_not_show_not_own_notifications(self):
		TradeRequestFactory.create_batch(3, profile=self.user.profile)

		other_user = UserWithProfileFactory.create()
		client = Client()
		client.force_login(other_user)

		response = client.get(reverse("notifications"))
		notif_amount = response.context["object_list"].count()

		self.assertEqual(notif_amount, 0)
