from django.test import TestCase, Client
from users.factories import UserWithProfileFactory
from django.urls import reverse
from public_tradelist.factories import TradeRequestFactory


# Create your tests here.
class PublicTradeListViewTest(TestCase):
    def setUp(self):
        self.user = UserWithProfileFactory.create()

    def test_it_opens_by_link(self):
        profile = self.user.profile
        client = Client()
        response = client.get(reverse("public_tradelist", args=[profile.trade_id]))

        self.assertEqual(response.status_code, 200)

    def test_it_shows_trade_requests(self):
        TradeRequestFactory.create_batch(3, profile=self.user.profile)
        client = Client()
        client.force_login(self.user)
        response = client.get(reverse("trade_requests"))
        tr_amount = response.context['object_list'].count()

        self.assertEqual(tr_amount, 3)
