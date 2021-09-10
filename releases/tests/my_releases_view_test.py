from django.test import Client
from django.urls import reverse_lazy, reverse
from releases.factories import ReleaseFactory
from users.factories import ProfileFactory, LabelFactory
from . import BaseClientTest


class MyReleasesViewTest(BaseClientTest):
    def test_it_shows_my_releases_page(self):
        response = self.client.get(reverse_lazy("my_releases"))

        self.assertEqual(response.status_code, 200)

    def test_it_redirects_unlogged_user(self):
        anonymous = Client()
        response = anonymous.get(reverse_lazy("my_releases"))

        self.assertRedirects(response, f"{reverse('login')}?next={reverse('my_releases')}")

    def test_it_shows_users_releases(self):
        # create logged in user's releases
        label = LabelFactory(profile=self.user.profile)
        ReleaseFactory.create_batch(2, profile=self.user.profile, label=label)

        # create another user's releases
        other_user_profile = ProfileFactory()
        other_label = LabelFactory(profile=other_user_profile)
        ReleaseFactory.create_batch(3, profile=other_user_profile, label=other_label)

        response = self.client.get(reverse('my_releases'))

        self.assertEqual(len(response.context["releases"]), 2)
        self.assertTrue(all([i.profile == self.user.profile for i in response.context["releases"]]))