from django.test import Client
from django.urls import reverse_lazy, reverse
from configuration.settings import BASE_DIR
from releases.factories import ReleaseFactory
from .base_client_test import BaseClientTest
from users.factories import UserWithProfileFactory


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
        user = UserWithProfileFactory.create()
        client = Client()
        client.force_login(user)
        release = ReleaseFactory.create(profile=user.profile)

        new_album_title = 'Some album title'

        with open(f"{BASE_DIR}/releases/test_files/dummy.jpg", 'rb') as dummy_jpg:
            with open(f"{BASE_DIR}/releases/test_files/dummy.mp3", 'rb') as dummy_mp3:
                response = client.post(reverse_lazy('edit_release', args=[release.id]), {
                    "band_name": release.band_name,
                    "country": release.country,
                    "album_title": new_album_title,
                    "release_date": "2021-01-01",
                    "label": release.label.id,
                    "base_style": release.base_style,
                    "cover_image": dummy_jpg,
                    "format": release.format,
                    "sample": dummy_mp3,
                    "media_format_details": "digipack, b2b",
                    "limited_edition": 1112
                })

        release.refresh_from_db()

        self.assertEqual(release.album_title, new_album_title)
        self.assertRedirects(response, reverse('my_releases'))
