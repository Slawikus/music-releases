from django.test import TestCase, Client
from users.factories import UserWithProfileFactory
from labels.factories import LabelFactory
from django.urls import reverse
from users.models import ProfileCurrency

class CreateProfileCurrencyViewTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = UserWithProfileFactory()
		self.client.force_login(self.user)

	def test_it_creates_currency(self):
		response = self.client.post(reverse('currency_create'), {
			'currency': "USD"
		})

		profile_currency = ProfileCurrency.objects.get(profile=self.user.profile)
		self.assertEqual(response.status_code, 302)
		self.assertEqual(profile_currency.currency, "USD")
