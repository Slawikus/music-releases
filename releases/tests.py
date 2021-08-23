from datetime import timedelta

from django.test import TestCase, Client, RequestFactory
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from configuration.settings import BASE_DIR

from releases.models import Release
from releases.factories import ReleaseFactory
from users.factories import ProfileFactory, LabelFactory, UserWithProfileFactory
from releases import views


def get_view_context(user, view_class):
    request = RequestFactory().get("/")
    request.user = user
    view = view_class()
    view.setup(request)
    view.object_list = view.get_queryset()

    return view.get_context_data()


class BaseClientTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserWithProfileFactory.create()
        self.client.force_login(self.user)


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
            ReleaseFactory.create(profile=self.user.profile,
                                  label=label,
                                  is_submitted=True,
                                  submitted_at=timezone.now() - timedelta(days=i)
                                  )

        context = get_view_context(self.user, views.RecentlySubmittedView)["releases"]
        datetime_sorted = self.check_datetime_sorted([i.submitted_at for i in context])

        self.assertEqual(len(context), 5)
        self.assertTrue(datetime_sorted)


class UpcomingViewTest(BaseClientTest):

    def test_time(self):
        response = self.client.get(reverse_lazy('upcoming_releases'))
        self.assertTrue(response.status_code, 200)

        # setup test releases
        label = LabelFactory(profile=self.user.profile)
        for i in range(10):
            ReleaseFactory.create(profile=self.user.profile, label=label)

        response = self.client.get(reverse('upcoming_releases'))

        self.assertTrue(all([rel.submitted_at > timezone.now() for rel in response.context["releases"]]))


class CreateReleaseTest(BaseClientTest):
    def test_it_shows_add_release_page(self):
        response = self.client.get(reverse_lazy('release_add'))

        self.assertEqual(response.status_code, 200)

    def test_it_creates_the_release(self):
        label = LabelFactory(profile=self.user.profile)

        album_title = 'Some Album Title'

        with open(f"{BASE_DIR}/releases/test_files/dummy.jpg", 'rb') as dummy_jpg:
            with open(f"{BASE_DIR}/releases/test_files/dummy.mp3", 'rb') as dummy_mp3:
                response = self.client.post(reverse_lazy('release_add'), {
                    "band_name": "test_band",
                    "country": "MC",
                    "album_title": album_title,
                    "release_date": "2021-01-01",
                    "submitted_at": "2021-08-18",
                    "label": label.id,
                    "base_style": "black_metal",
                    "cover_image": dummy_jpg,
                    "format": "CD",
                    "sample": dummy_mp3,
                    "limited_edition": 10,
                    "media_format_details": "something",

                })

        self.assertEqual(Release.objects.count(), 1)
        self.assertEqual(Release.objects.first().album_title, album_title)
        self.assertRedirects(response, reverse('home'))


class EditReleaseViewTest(BaseClientTest):
    def test_it_shows_release_edit_page(self):
        release = ReleaseFactory.create(is_submitted=True, profile=self.user.profile)

        response = self.client.get(reverse("edit_release", args=[release.id]))

        self.assertEqual(response.status_code, 200)

    def test_it_redirects_unlogged_user(self):
        release = ReleaseFactory.create(is_submitted=True)

        anonymous = Client()
        response = anonymous.get(reverse("edit_release", args=[release.id]))

        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse_lazy('edit_release', args=[release.id])}"
        )

    def test_it_forbids_editing_not_own_releases(self):
        release = ReleaseFactory.create(is_submitted=True)

        response = self.client.get(reverse("edit_release", args=[release.id]))

        self.assertEqual(response.status_code, 403)

    def test_it_updates_the_release(self):
        release = ReleaseFactory.create(profile=self.user.profile)

        new_album_title = 'Some album title'

        with open(f"{BASE_DIR}/releases/test_files/dummy.jpg", 'rb') as dummy_jpg:
            with open(f"{BASE_DIR}/releases/test_files/dummy.mp3", 'rb') as dummy_mp3:
                response = self.client.post(reverse_lazy('edit_release', args=[release.id]), {
                    "band_name": release.band_name,
                    "country": release.country,
                    "album_title": new_album_title,
                    "release_date": release.release_date,
                    "submitted_at": release.submitted_at,
                    "label": release.label.id,
                    "base_style": release.base_style,
                    "cover_image": dummy_jpg,
                    "format": release.format,
                    "sample": dummy_mp3,
                })

        release.refresh_from_db()

        self.assertEqual(release.album_title, new_album_title)
        self.assertRedirects(response, reverse('my_releases'))

    def test_excel(self):
        client = Client()
        response = client.get(reverse_lazy("get_example_excel"))
        self.assertEqual(response.status_code, 200)