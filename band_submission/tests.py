from django.test import TestCase, Client, RequestFactory
from django.urls import reverse

from users.factories import UserWithProfileFactory, LabelFactory
from users.views import BandSubmissionsView
from .models import BandSubmission
from configuration.settings import BASE_DIR
import uuid


# Create your tests here.
class BandSubmissionTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserWithProfileFactory.create()
        self.client.force_login(self.user)
        self.uuid = self.user.profile.submission_uuid

    def test_it_opens_form_by_link(self):
        client = Client()
        response = client.get(reverse("band_submission", args=[self.uuid]))
        self.assertEqual(response.status_code, 200)

    def test_it_forbids_wrong_uuid_link(self):
        client = Client()
        response = client.get(reverse("band_submission", args=[uuid.uuid4()]))
        self.assertEqual(response.status_code, 403)

    def test_it_saves_submission(self):
        label = LabelFactory(profile=self.user.profile)
        client = Client()
        with open(f"{BASE_DIR}/releases/test_files/dummy.jpg", 'rb') as dummy_jpg:
            with open(f"{BASE_DIR}/releases/test_files/dummy.mp3", 'rb') as dummy_mp3:
                response = client.post(reverse("band_submission", args=[self.uuid]), {
                    "name": "test",
                    "demo_sample": dummy_mp3,
                    "logo": dummy_jpg,
                    "email": "test@gmail.com",
                    "biography": "some description"
                })

        self.assertEqual(BandSubmission.objects.count(), 1)

    def test_it_shows_submission_in_profile(self):
        BandSubmission.objects.create(profile=self.user.profile,
                                      name="test",
                                      demo_sample="test/path",
                                      email="test@gmail.com",
                                      biography="Armin Van Buren - BLAH BLAH BLAH")
        request = RequestFactory().get(reverse("submissions"))
        request.user = self.user
        view = BandSubmissionsView(request=request)

        self.assertEqual(view.get_queryset().count(), 1)
