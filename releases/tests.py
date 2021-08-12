from django.test import TestCase, Client, RequestFactory
from django.urls import reverse_lazy, reverse

from django.utils import timezone
from datetime import timedelta

from releases.models import Release
from users.models import User
from .views import (UpcomingReleasesView,
                    MyReleasesView,
                    AllReleaseView,
                    RecentlySubmittedView
                    )
from .factories import (
    ReleaseFactory,
    ProfileFactory,
    LabelFactory,
)


def get_view_context(user, view_class):
    request = RequestFactory().get("/")
    request.user = user
    view = view_class()
    view.setup(request)
    view.object_list = view.get_queryset()

    return view.get_context_data()


# Create your tests here.
class BaseClientTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('lotus', password='qweytr21')
        self.client.login(username='lotus', password='qweytr21')


class MyReleasesViewTest(BaseClientTest):

    def test_response(self):
        response = self.client.get(reverse_lazy("my_releases"))
        self.assertEqual(response.status_code, 200)

    def test_un_logged_user(self):
        anonymous = Client()
        response = anonymous.get(reverse_lazy("my_releases"))
        self.assertEqual(response.status_code, 302)

    def test_security(self):
        # create logged in user's releases
        label = LabelFactory(profile=self.user.profile)
        ReleaseFactory.create_batch(2, profile=self.user.profile, label=label)
        # create another user's releases
        other_user_profile = ProfileFactory()
        other_label = LabelFactory(profile=other_user_profile)
        ReleaseFactory.create_batch(3, profile=other_user_profile, label=other_label)

        context = get_view_context(self.user, MyReleasesView)

        self.assertEqual(len(context["releases"]), 2)
        self.assertTrue(all([i.profile == self.user.profile for i in context["releases"]]))


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

        context = get_view_context(self.user, AllReleaseView)

        self.assertEqual(len(context["releases"]), 3)


class RecentlySubmittedViewTest(BaseClientTest):

    def test_response(self):
        response = self.client.get(reverse_lazy('recently_submitted'))
        self.assertEqual(response.status_code, 200)

    def test_time_sort(self):
        label = LabelFactory(profile=self.user.profile)

        ReleaseFactory.create_batch(3, profile=self.user.profile, label=label)
        # create releases with random datetime and submitted
        for i in [3, 2, 5, 1, 4]:
            ReleaseFactory.create(profile=self.user.profile,
                                  label=label,
                                  is_submitted=True,
                                  submitted_at=timezone.now() - timedelta(days=i)
                                  )

        context = get_view_context(self.user, RecentlySubmittedView)["releases"]

        self.assertEqual(len(context), 5)


class UpcomingViewTest(BaseClientTest):

    def test_time(self):
        response = self.client.get(reverse_lazy('upcoming_releases'))
        self.assertTrue(response.status_code, 200)

        # setup test releases
        profile = ProfileFactory.create()
        label = LabelFactory(profile=profile)
        for i in range(10):
            ReleaseFactory(profile=profile, label=label)
        context = get_view_context(self.user, UpcomingReleasesView)
        # check if all release dates are in future
        self.assertTrue(all([rel.release_date < timezone.now() for rel in context["releases"]]))


class CreateReleaseTest(BaseClientTest):

    def test_creation(self):
        response = self.client.get(reverse_lazy('release_add'))
        self.assertTrue(response.status_code, 200)

        profile = ProfileFactory.create()
        label = LabelFactory(profile=profile)
        edit_response = self.client.post(reverse_lazy('release_add'), {
            "profile": profile.id,
            "band_name": "test_band", # this value will be checked bellow
            "country": "Monaco",
            "album_title": "test album",
            "release_date": "2021-01-01",
            "label": label.id,
            "base_style": "Black Metal",
            "cover_image": "path/to/image",
            "format": "CD",
            "sample": "path/to/sample"
        })
        self.assertEqual(edit_response.status_code, 200)
        self.assertTrue(Release.objects.filter(band_name="test_band").exists())

class EditReleaseView(BaseClientTest):

    def test_security(self):

        label = LabelFactory(profile=self.user.profile)
        release = ReleaseFactory.create(profile=self.user.profile, label=label, is_submitted=True)

        anonymous = Client()
        response = anonymous.get(reverse("edit_release", kwargs={"pk": release.id}))

        self.assertEqual(response.status_code, 302)