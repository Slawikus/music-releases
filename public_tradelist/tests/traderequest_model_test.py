from django.test import TestCase, Client
from public_tradelist.factories import TradeRequestFactory
from users.factories import UserWithProfileFactory
from notifications.models import Notification


class TradeRequestModelTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = UserWithProfileFactory()
		self.client.force_login(self.user)

	def test_it_creates_notification(self):
		TradeRequestFactory.create_batch(3, profile=self.user.profile)
		TradeRequestFactory.create_batch(2)
		notif_amount = Notification.objects.filter(profile=self.user.profile).count()

		self.assertEqual(notif_amount, 3)
