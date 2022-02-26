from django.test import TestCase, Client
from users.factories import UserWithProfileFactory
from django.urls import reverse
from releases.factories import ReleaseFactory


class UpdateTradesInfoViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserWithProfileFactory()
        self.client.force_login(self.user)

    def test_it_updates_trade_info(self):
        release = ReleaseFactory.create(profile=self.user.profile)
        self.client.post(reverse('release_trades_info_edit', args=[release.id]), {
            'available_for_trade': True,
            'trade_points': 1
        })
        release.refresh_from_db()
        self.assertTrue(release.releasetradesinfo.available_for_trade)
