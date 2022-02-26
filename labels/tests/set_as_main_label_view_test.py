from django.test import TestCase, Client
from users.factories import UserWithProfileFactory
from labels.factories import LabelFactory
from django.urls import reverse


class SetAsMainLabelViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserWithProfileFactory()
        self.client.force_login(self.user)

    def test_it_changes_main_label(self):
        label = LabelFactory.create(profile=self.user.profile)
        self.client.post(reverse('label_set_as_main', args=[label.id]))
        label.refresh_from_db()
        self.assertTrue(label.is_main)
