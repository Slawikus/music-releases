from django.test import TestCase, Client, RequestFactory
from django.urls import reverse

from users.factories import UserWithProfileFactory, LabelFactory
from users.views import BandSubmissionsView
from .factories import BandSubmissionLinkFactory
from .models import BandSubmission
from configuration.settings import BASE_DIR


# Create your tests here.
class BandSubmissionTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserWithProfileFactory.create()
        self.client.force_login(self.user)


    def test_it_opens_form_by_link(self):
        label = LabelFactory(profile=self.user.profile)
        link = BandSubmissionLinkFactory.create(profile=self.user.profile, label=label).slug
        client = Client()
        response = client.get(reverse("band_submission", args=[link]))
        self.assertEqual(response.status_code, 200)

    def test_it_saves_submission(self):
        label = LabelFactory(profile=self.user.profile)
        link = BandSubmissionLinkFactory.create(profile=self.user.profile, label=label).slug
        client = Client()
        with open(f"{BASE_DIR}/releases/test_files/dummy.jpg", 'rb') as dummy_jpg:
            with open(f"{BASE_DIR}/releases/test_files/dummy.mp3", 'rb') as dummy_mp3:
                response = client.post(reverse("band_submission", args=[link]), {
                    "name": "test",
                    "demo_sample": dummy_mp3,
                    "logo": dummy_jpg,
                    "email": "test@gmail.com",
                    "biography": "some description"
                })

        self.assertEqual(BandSubmission.objects.count(), 1)

    def test_it_shows_submission_in_profile(self):


        request = RequestFactory().get(reverse("submissions"))
        request.user = self.user
        view = BandSubmissionsView(request)

        self.assertEqual(view.object_list.count(), 1)