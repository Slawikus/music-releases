from django.test import TestCase, Client
from releases.factories import ReleaseFactory
from users.factories import UserWithProfileFactory
from django.urls import reverse


class AddToWishlistViewTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = UserWithProfileFactory()
		self.client.force_login(self.user)

	def test_it_adds_to_wishlist(self):
		release = ReleaseFactory.create()
		self.client.post(reverse('add_to_wishlist', args=[release.id]))
		self.assertTrue(self.user.profile.wishlist.filter(id=release.id).exists())
