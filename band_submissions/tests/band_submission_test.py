from django.test import TestCase, Client
from django.urls import reverse

from users.factories import UserWithProfileFactory
from band_submissions.models import BandSubmission
from configuration.settings import BASE_DIR
import uuid


# Create your tests here.
class BandSubmissionTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserWithProfileFactory.create()
        self.uuid = self.user.profile.submission_uuid

    def test_it_opens_form_by_link(self):
        response = self.client.get(reverse("band_submission", args=[self.uuid]))
        self.assertEqual(response.status_code, 200)

    def test_it_forbids_wrong_uuid_link(self):
        client = Client()
        response = client.get(reverse("band_submission", args=[uuid.uuid4()]))
        self.assertEqual(response.status_code, 404)

    def test_it_saves_submission(self):
        client = Client()
        with open(f"{BASE_DIR}/releases/test_files/dummy.jpg", 'rb') as dummy_jpg:
            with open(f"{BASE_DIR}/releases/test_files/dummy.mp3", 'rb') as dummy_mp3:
                with open(f"{BASE_DIR}/band_submissions/test_files/album.rar", 'rb') as rar_file:
                    response = client.post(reverse("band_submission", args=[self.uuid]), {
                        "name": "test",
                        "album": rar_file,
                        "best_track": dummy_mp3,
                        "front_cover": dummy_jpg,
                        "email": "test@gmail.com",
                        "phone_number": "+996222000000",
                        "biography": "some description"
                    })

        self.assertEqual(BandSubmission.objects.last().profile, self.user.profile)
        self.assertEqual(BandSubmission.objects.count(), 1)
