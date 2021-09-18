from django.test import TestCase, Client
from users.factories import UserWithProfileFactory, LabelFactory
from releases.factories import ReleaseFactory
from django.urls import reverse


class LabelDetailViewTest(TestCase):
	def test_it_shows_labels_releases(self):
		user = UserWithProfileFactory.create()
		client = Client()
		client.force_login(user)

		label = LabelFactory.create(profile=user.profile)
		releases = ReleaseFactory.create_batch(3, profile=user.profile, label=label)

		response = client.get(reverse("label_detail", args=[label.id]))
		release_amount = response.context['label'].releases.count()

		self.assertEqual(release_amount, 3)
