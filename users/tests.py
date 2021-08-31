from django.test import TestCase, RequestFactory, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .views import BandSubmissionsView
from band_submissions.factories import BandSubmissionFactory


class SignupPageTests(TestCase):
    def setUp(self):
        self.email = 'newuser@email.com'
        self.password = 'TestPassword1234'

    def test_signup_page_status_code(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.email, self.password)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)

        self.user = get_user_model().objects.get(email=self.email)
        self.assertEquals(self.user.check_password("TestPassword1234"), True)

    def test_it_shows_submission_in_profile(self):
        new_user = get_user_model().objects.create_user(self.email, self.password)
        BandSubmissionFactory.create_batch(5, profile=new_user.profile)
        client = Client()
        client.force_login(new_user)
        response = client.get(reverse("submissions"))

        self.assertEqual(response.context["submissions"].count(), 5)
