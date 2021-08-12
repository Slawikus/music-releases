from django.test import TestCase, Client, RequestFactory
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model

from datetime import date

from users.models import User, Label
from .views import UpcomingReleasesView, MyReleasesView
from .factories import (
    ReleaseFactory,
    ProfileFactory,
    LabelFactory,
    UserFactory
)

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

    def test_security(self):
        # create logged in user's releases
        label = LabelFactory(profile=self.user.profile)
        ReleaseFactory.create_batch(2, profile=self.user.profile, label=label)
        # create another user's releases
        other_user_profile = ProfileFactory()
        other_label = LabelFactory(profile=other_user_profile)
        ReleaseFactory.create_batch(3, profile=other_user_profile, label=other_label)

        request = RequestFactory().get("/")
        view = MyReleasesView(context_object_name='releases')
        view.setup(request)
        view.object_list = view.get_queryset()
        context = view.get_context_data()

        self.assertEqual(len(context["releases"]), 2)
        self.assertTrue(all([i.profile == self.user.profile for i in context["releases"]]))


class AllReleasesViewTest(TestCase):

    def test_response(self):
        response = self.client.get(reverse_lazy("all_releases"))
        self.assertEqual(response.status_code, 200)


class RecentlySubmittedReleasesView(BaseClientTest):

    def test_response(self):
        response = self.client.get(reverse_lazy('recently_submitted'))
        self.assertEqual(response.status_code, 200)


class UpcomingViewTest(BaseClientTest):

    def test_time(self):
        response = self.client.get(reverse_lazy('upcoming_releases'))
        self.assertTrue(response.status_code, 200)

        # setup test releases
        profile = ProfileFactory.create()
        label = LabelFactory(profile=profile)
        for i in range(10):
            ReleaseFactory(profile=profile, label=label)

        # setup view
        request = RequestFactory().get("/")
        view = UpcomingReleasesView(context_object_name='releases')
        view.setup(request)
        view.object_list = view.get_queryset()
        context = view.get_context_data()
        # check if all release dates are in future
        self.assertTrue(all([rel.release_date < date.today() for rel in context["releases"]]))


class CreateReleaseTest(BaseClientTest):

    def test_creation(self):
        response = self.client.get(reverse_lazy('release_add'))
        self.assertTrue(response.status_code, 200)

        profile = ProfileFactory.create()
        label = LabelFactory(profile=profile)
        edit_response = self.client.post(reverse_lazy('release_add'), {
            "profile": profile.id,
            "band_name": "test_band",
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


class EditReleaseView(BaseClientTest):

    def test_security(self):
        response = self.client.get(reverse("edit_release", kwargs={"pk": 5}))
        self.assertEqual(response.status_code, 404)
