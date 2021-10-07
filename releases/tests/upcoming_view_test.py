from django.urls import reverse_lazy, reverse
from django.utils import timezone
from releases.factories import ReleaseFactory
from labels.factories import LabelFactory
from . import BaseClientTest


class UpcomingViewTest(BaseClientTest):

    def test_time(self):

        response = self.client.get(reverse_lazy('upcoming_releases'))
        self.assertTrue(response.status_code, 200)

        label = LabelFactory(profile=self.user.profile)
        for i in range(10):
            ReleaseFactory.create(profile=self.user.profile, label=label)

        response = self.client.get(reverse('upcoming_releases'))

        self.assertTrue(all([rel.submitted_at > timezone.now() for rel in response.context["releases"]]))