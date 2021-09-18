from django.test import TestCase, Client
from users.factories import UserWithProfileFactory
from public_tradelist.factories import TradeRequestFactory
from notifications.models import Notification
from django.urls import reverse


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
