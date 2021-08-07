from django.test import TestCase, Client
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

# Create your tests here.
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        User = get_user_model()
        User.objects.create_user('lotus', password='qweytr21')
        self.assertTrue(self.client.login(username='lotus', password='qweytr21'))

    def test_my_releases(self):

        response = self.client.get(reverse_lazy("my_releases"))
        self.assertTrue(response.status_code, 200)

    def test_all_releases(self):

        response = self.client.get(reverse_lazy("all_releases"))
        self.assertTrue(response.status_code, 200)

    def test_recently_submitted(self):

        response = self.client.get(reverse_lazy('recently_submitted'))
        self.assertTrue(response.status_code, 200)

    def test_upcoming(self):

        response = self.client.get(reverse_lazy('upcoming_releases'))
        self.assertTrue(response.status_code, 200)

    def test_create_release(self):
        response = self.client.get(reverse_lazy('release_add'))
        self.assertTrue(response.status_code, 200)