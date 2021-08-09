from django.test import TestCase, Client, RequestFactory
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model

from datetime import date

from users.models import User, Label
from .views import UpcomingReleasesView

# Create your tests here.
class BaseClientTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = get_user_model()
        self.user.objects.create_user('lotus', password='qweytr21')
        self.client.login(username='lotus', password='qweytr21')


class MyReleasesViewTest(BaseClientTest):

    def test_response(self):
        response = self.client.get(reverse_lazy("my_releases"))
        self.assertEqual(response.status_code, 200)


class AllReleasesViewTest(BaseClientTest):

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

        profile = User.objects.first().profile
        label = Label.objects.create(name='testing label', profile=profile)
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
