from django.test import TestCase, Client
from users.factories import UserWithProfileFactory
from django.urls import reverse
from public_tradelist.factories import TradeRequestFactory
from releases.factories import ReleaseFactory
from users.factories import ProfileCurrencyFactory
from releases.models import ReleaseWholesaleInfo, ReleaseTradesInfo
from public_tradelist.models import TradeRequest
from releases.models import Release


# Create your tests here.
class PublicTradeListViewTest(TestCase):
    def setUp(self):
        self.user = UserWithProfileFactory.create()

    def test_it_opens_by_link(self):
        profile = self.user.profile
        client = Client()
        response = client.get(reverse("public_tradelist", args=[profile.trade_id]))

        self.assertEqual(response.status_code, 200)

    def create_release_ready_for_public_tradelist(self):

        release = ReleaseFactory.create(profile=self.user.profile)
        ProfileCurrencyFactory.create(profile=self.user.profile)

        release.is_submitted = True
        release.releasewholesaleinfo.available_for_wholesale = True
        release.releasetradesinfo.available_for_trade = True
        release.save()

        return release

    # def test_it_shows_public_tradelist(self):
    #
    #     self.create_release_ready_for_public_tradelist()
    #
    #     trade_id = str(self.user.profile.trade_id)
    #     response = self.client.get(reverse('public_tradelist', args=[trade_id]))
    #
    #     releases_amount = response.context['object_list'].count()
    #     self.assertEqual(releases_amount, 1)

    def test_it_accepts_trade_request(self):

        release = self.create_release_ready_for_public_tradelist()

        trade_id = str(self.user.profile.trade_id)
        ex = Release.objects.tradelist_items_for_profile(self.user.profile)
        self.client.post(reverse('public_tradelist', args=[trade_id]), {
            'items': f'{release.id}:10'
        })
        self.assertEqual(TradeRequest.objects.count(), 1)


    def test_it_shows_trade_requests(self):
        TradeRequestFactory.create_batch(3, profile=self.user.profile)
        client = Client()
        client.force_login(self.user)
        response = client.get(reverse("trade_requests"))
        tr_amount = response.context['object_list'].count()

        self.assertEqual(tr_amount, 3)
