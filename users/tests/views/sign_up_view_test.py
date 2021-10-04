from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from users.models import Invitation, User
from band_submissions.factories import BandSubmissionFactory
from users.factories import ProfileFactory


class SignUpViewTest(TestCase):
    def setUp(self):
        self.name = "John Doe"
        self.email = 'newuser@email.com'
        self.password = 'TestPassword1234'
        self.user = get_user_model().objects.create(name=self.name, email=self.email, password=self.password)

    def test_it_can_use_invitation(self):
        invitation = Invitation.objects.last()
        client = Client()
        response = client.get(reverse("signup", args=[invitation.public_id]))
        self.assertEqual(response.status_code, 200)

    def test_it_registers_new_user(self):
        invitation = Invitation.objects.last()
        client = Client()

        email = "test@gmail.com"
        response = client.post(reverse("signup", args=[invitation.public_id]), {
            "name": "Lord Demogorgon",
            "email": email,
            "password1": "test123456",
            "password2": "test123456",
            "main_label_name": "Metal Blade GmbH",
            "country": "AF"
        })

        self.assertRedirects(response, expected_url='/')
        self.assertTrue(User.objects.filter(email=email).exists())
        self.assertEqual(Invitation.objects.filter(profile__user__email=email).count(), 3)

        client.post(reverse("logout"))
        response = client.post(reverse("login"), {
            "email": email,
            "password": "test123456"
        })

        user = User.objects.get(email=email)
        self.assertTrue(user.is_authenticated())


    def test_it_would_not_open_inactive_invitation(self):
        invitation = Invitation.objects.last()
        invitation.is_active = False
        invitation.save()
        client = Client()
        response = client.get(reverse("signup", args=[invitation.public_id]))
        message = "Sorry, your invitation link is already been used and not valid anymore"
        self.assertEqual(response.headers["Content-Type"], message)

    def test_it_shows_submission_in_profile(self):
        profile = ProfileFactory.create()
        BandSubmissionFactory.create_batch(5, profile=profile)
        client = Client()
        client.force_login(profile.user)
        response = client.get(reverse("submissions"))

        self.assertEqual(response.context["submissions"].count(), 5)
