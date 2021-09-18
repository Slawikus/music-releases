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



class NotificationRedirectViewTest(TestCase):
	def setUp(self):
		self.user = UserWithProfileFactory.create()
		self.client = Client()
		self.client.force_login(self.user)

	def test_it_redirects_and_closes_notification(self):

		trade_request = TradeRequestFactory.create(profile=self.user.profile)
		notification = Notification.objects.last()
		response = self.client.get(reverse("notif_redirect", args=[notification.id]))
		expected_url = reverse("trade_details", args=[trade_request.id])

		self.assertRedirects(response, expected_url=expected_url)

		self.assertEqual(notification.is_viewed, False)
