from django.test import TestCase, Client
from django.urls import reverse
from releases.factories import ReleaseFactory
from users.factories import UserWithProfileFactory


class ReleaseDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserWithProfileFactory()
        self.client.force_login(self.user)

    def test_it_shows_release_detail(self):
        release = ReleaseFactory.create(profile=self.user.profile)
        response = self.client.get(reverse("release_detail", args=[release.id]))

        self.assertEqual(response.status_code, 200)

    def test_it_does_not_show_not_submitted_release_to_other_user(self):
        release = ReleaseFactory.create(is_submitted=False)
        response = self.client.get(reverse("release_detail", args=[release.id]))

        self.assertEqual(response.status_code, 403)

    def test_it_redirects_unlogged_user(self):
        release = ReleaseFactory.create(is_submitted=True)
        client = Client()
        response = client.get(reverse("release_detail", args=[release.id]))

        self.assertEqual(response.status_code, 302)
