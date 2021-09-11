from django.test import TestCase, Client
from users.factories import UserWithProfileFactory
from django.urls import reverse


# Create your tests here.
class PublicTradeListViewTest(TestCase):
    def setUp(self):
        self.user = UserWithProfileFactory.create()

    def test_it_opens_by_link(self):
        profile = self.user.profile
        client = Client()
        response = client.get(reverse("public_tradelist", args=[profile.trade_id]))

        self.assertEqual(response.status_code, 200)
