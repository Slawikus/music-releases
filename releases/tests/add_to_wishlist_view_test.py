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

	def test_it_does_not_make_duplicates(self):
		release = ReleaseFactory.create()
		self.client.post(reverse('add_to_wishlist', args=[release.id]))
		self.client.post(reverse('add_to_wishlist', args=[release.id]))

		self.assertEqual(self.user.profile.wishlist.filter(id=release.id).count(), 1)

	def test_it_one_cannot_see_another_users_wishlist(self):
		release = ReleaseFactory.create()
		self.client.post(reverse('add_to_wishlist', args=[release.id]))
		self.assertEqual(self.user.profile.wishlist.filter(id=release.id).count(), 1)

		client = Client()
		another_user = UserWithProfileFactory()
		client.force_login(another_user)

		response = client.get(reverse("wishlist"))

		self.assertEqual(response.context["object_list"].count(), 0)


	def test_it_redirects_unlogged_user(self):
		client = Client()
		response = client.get(reverse('wishlist'))
		self.assertEqual(response.status_code, 302)
