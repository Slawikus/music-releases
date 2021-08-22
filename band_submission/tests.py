from django.test import TestCase, Client
from users.models import Label
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your tests here.
class BandSubmissionLinkTest(TestCase):
    def setUp(self):
        self.email = "test@gmail.com"
        self.password = "test123456"
        self.user = get_user_model().objects.create(self.email, self.password)

    def test_it_creates_submission_link(self):
        client = Client()
        client.force_login(self.user)
        response = client.post(reverse("submission_links"),)