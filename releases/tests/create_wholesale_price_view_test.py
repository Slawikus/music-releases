from django.test import TestCase, Client
from users.factories import UserWithProfileFactory
from django.urls import reverse
from releases.factories import ReleaseFactory
from users.models import ProfileCurrency


class CreateWholesalePriceViewTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = UserWithProfileFactory()
		self.client.force_login(self.user)

	def test_it_creates_price(self):
		release = ReleaseFactory.create(profile=self.user.profile)
		profile_currency = ProfileCurrency.objects.create(profile=self.user.profile)
		self.client.post(reverse('release_wholesale_price_add', args=[release.id]),{
			'currency': profile_currency.id,
			'price': 200
		})

		price_items = release.wholesale_prices.filter(currency=profile_currency.id)
		self.assertTrue(price_items.exists)
		self.assertEqual(price_items[0].price, 200)
