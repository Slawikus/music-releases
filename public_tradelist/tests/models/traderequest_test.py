from django.test import TestCase
from public_tradelist.factories import TradeRequestFactory
from notifications.models import Notification


class TradeRequestTest(TestCase):

	def test_it_creates_notification(self):
		trade_request = TradeRequestFactory.create()
		notif_amount = Notification.objects.count()

		self.assertEqual(notif_amount, 1)

		trade_request.name = "test name"
		trade_request.save()

		notif_amount = Notification.objects.count()

		self.assertEqual(notif_amount, 1)
