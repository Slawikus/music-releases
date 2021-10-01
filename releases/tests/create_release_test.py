from django.urls import reverse_lazy, reverse
from configuration.settings import BASE_DIR
from .base_client_test import BaseClientTest
from releases.models import Release
from users.factories import LabelFactory



class CreateReleaseTest(BaseClientTest):
    def test_it_shows_add_release_page(self):
        response = self.client.get(reverse_lazy('release_add'))

        self.assertEqual(response.status_code, 200)

    def test_it_creates_and_submits_the_release(self):
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

        release = Release.objects.get(album_title=album_title)
        self.client.post(reverse('release_submit', args=[release.id]))
        release.refresh_from_db()
        self.assertTrue(release.is_submitted)

    def test_it_creates_not_full_release(self):
        band_name = 'test_band'
        response = self.client.post(reverse_lazy('release_add'), {
            'band_name': band_name,
            'album_title': 'test_title',
            'format': 'CD'
        })

        self.assertTrue(Release.objects.filter(band_name=band_name).exists())
        self.assertRedirects(response, expected_url=reverse_lazy('my_releases'))

    def test_it_forbids_submit_not_full_release(self):
        release = Release.objects.create(
            profile=self.user.profile,
            band_name='test_band',
            album_title='test_title'
        )

        self.client.post(reverse('release_submit', args=[release.id]))
        release.refresh_from_db()
        self.assertFalse(release.is_submitted)
