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
        response = self.client.get(reverse("notif_redirect", args=[notification.pk]))
        expected_url = reverse("trade_details", args=[trade_request.id])

        self.assertRedirects(response, expected_url=expected_url)

        notification.refresh_from_db()
        self.assertEqual(notification.is_viewed, True)

    def test_it_forbids_redirect_to_others_notification(self):
        TradeRequestFactory.create(profile=self.user.profile)
        notification = Notification.objects.last()

        other_user = UserWithProfileFactory.create()
        client = Client()
        client.force_login(other_user)

        response = client.get(reverse("notif_redirect", args=[notification.pk]))

        self.assertEqual(response.status_code, 403)
