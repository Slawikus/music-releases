from django.test import TestCase, Client
from users.factories import UserWithProfileFactory


class BaseClientTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserWithProfileFactory.create()
        self.client.force_login(self.user)