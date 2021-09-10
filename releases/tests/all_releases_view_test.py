from django.test import Client
from django.urls import reverse_lazy, reverse
from releases.factories import ReleaseFactory
from users.factories import ProfileFactory, LabelFactory
from . import BaseClientTest

class AllReleasesViewTest(BaseClientTest):
    def test_response(self):
        response = self.client.get(reverse_lazy("all_releases"))
        self.assertEqual(response.status_code, 200)

    def test_un_logged_user(self):
        anonymous = Client()
        response = anonymous.get(reverse_lazy("all_releases"))
        self.assertEqual(response.status_code, 302)

    def test_submits(self):
        # create logged in user's releases
        label = LabelFactory(profile=self.user.profile)
        ReleaseFactory.create_batch(2, profile=self.user.profile, label=label)
        ReleaseFactory.create(profile=self.user.profile, label=label, is_submitted=True)
        # create another user's releases
        other_user_profile = ProfileFactory()
        other_label = LabelFactory(profile=other_user_profile)
        ReleaseFactory.create_batch(2, profile=other_user_profile, label=other_label)
        ReleaseFactory.create_batch(2, profile=other_user_profile, label=other_label, is_submitted=True)

        response = self.client.get(reverse('all_releases'))

        self.assertEqual(len(response.context["releases"]), 3)
