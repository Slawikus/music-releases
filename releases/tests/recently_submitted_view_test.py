from datetime import timedelta
from django.urls import reverse_lazy
from django.utils import timezone
from releases.factories import ReleaseFactory, SubmittedReleaseFactory
from labels.factories import LabelFactory
from releases import views
from . import BaseClientTest
from .get_view_context import get_view_context


class RecentlySubmittedViewTest(BaseClientTest):
    def test_response(self):
        response = self.client.get(reverse_lazy('recently_submitted'))
        self.assertEqual(response.status_code, 200)

    @staticmethod
    def check_datetime_sorted(datetime) -> bool:
        for i in range(1, len(datetime)):
            if datetime[i] > datetime[i - 1]:
                return False
        return True

    def test_datetime(self):
        label = LabelFactory(profile=self.user.profile)

        ReleaseFactory.create_batch(3, profile=self.user.profile, label=label)
        # create releases with random datetime and submitted
        for i in [3, 2, 5, 1, 4]:
            SubmittedReleaseFactory.create(profile=self.user.profile,
                                  label=label,
                                  submitted_at=timezone.now() - timedelta(days=i)
                                  )

        context = get_view_context(self.user, views.RecentlySubmittedView)["releases"]
        datetime_sorted = self.check_datetime_sorted([i.submitted_at for i in context])

        self.assertEqual(len(context), 5)
        self.assertTrue(datetime_sorted)

