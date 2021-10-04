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
        self.client = Client()
        self.client.force_login(self.user)

    def test_it_opens_by_link(self):
        profile = self.user.profile
        client = Client()
        response = client.get(reverse("public_tradelist", args=[profile.trade_id]))

        self.assertEqual(response.status_code, 200)

    def create_release_ready_for_public_tradelist(self):

        release = ReleaseFactory.create(profile=self.user.profile)
        rwi = ReleaseWholesaleInfo.objects.get(release=release)
        rwi.available_for_wholesale = True
        rwi.save()

        rti = ReleaseTradesInfo.objects.get(release=release)
        rti.available_for_trade = True
        rti.save()
        release.is_submitted = True
        release.save()

        return release

    def test_it_shows_public_tradelist(self):

        self.create_release_ready_for_public_tradelist()

        trade_id = str(self.user.profile.trade_id)
        response = self.client.get(reverse('public_tradelist', args=[trade_id]))

        releases_amount = response.context['releases'].count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(releases_amount, 1)

    def test_it_accepts_trade_request(self):

        release = self.create_release_ready_for_public_tradelist()

        trade_id = str(self.user.profile.trade_id)
        ex = Release.objects.tradelist_items_for_profile(self.user.profile)
        response = self.client.post(reverse('public_tradelist', args=[trade_id]), {
            'name': 'test',
            'email': 'test@gmail.com',
            'items': f'{release.id}:10'
        })

        self.assertRedirects(response, expected_url="/")
        self.assertEqual(TradeRequest.objects.count(), 1)


    def test_it_shows_trade_requests(self):
        TradeRequestFactory.create_batch(3, profile=self.user.profile)
        client = Client()
        client.force_login(self.user)
        response = client.get(reverse("trade_requests"))
        tr_amount = response.context['object_list'].count()

        self.assertEqual(tr_amount, 3)
