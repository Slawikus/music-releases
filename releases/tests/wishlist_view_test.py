from django.test import TestCase, Client
from releases.factories import ReleaseFactory
from users.factories import UserWithProfileFactory


class WishlistViewTest(TestCase):
	def setUp(self):
		self.user = UserWithProfileFactory()
		self.client = Client()
		self.client.force_login(self.user)

	def test_it_shows_wishlist(self):
		rel1 = ReleaseFactory()
		rel2 = ReleaseFactory()
		wishlist = self.user.profile.wishlist
		wishlist.add(rel1)
		wishlist.add(rel2)

		self.assertEqual(wishlist.count(), 2)

