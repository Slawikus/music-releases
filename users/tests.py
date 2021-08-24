from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Invitation


class SignupPageTests(TestCase):
    def setUp(self):
        self.email = 'newuser@email.com'
        self.password = 'TestPassword1234'
        self.user = get_user_model().objects.create(email=self.email, password=self.password)

    def test_it_creates_invitations(self):
        amount = Invitation.objects.count()
        self.assertEqual(amount, 3)

    def test_it_can_use_invitation(self):
        invitation = Invitation.objects.last()
        client = Client()
        response = client.get(reverse("signup", args=[invitation.uuid]))
        self.assertEqual(response.status_code, 200)

    def test_it_would_not_open_inactive_invitation(self):
        invitation = Invitation.objects.last()
        invitation.active = False
        invitation.save()
        client = Client()
        response = client.get(reverse("signup", args=[invitation.uuid]))
        self.assertEqual(response.status_code, 403)