from django.urls import reverse_lazy, reverse
from configuration.settings import BASE_DIR
from .base_client_test import BaseClientTest
from releases.models import Release
from users.factories import LabelFactory



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
                    "base_style": "Classical",
                    "cover_image": dummy_jpg,
                    "format": "CD",
                    "sample": dummy_mp3,
                    "limited_edition": 10,
                    "media_format_details": "something",

                })

        self.assertEqual(Release.objects.count(), 1)
        self.assertEqual(Release.objects.first().album_title, album_title)
        self.assertRedirects(response, reverse("my_releases"))