from django.views.generic import ListView
from releases.models import Release

class WishlistView(ListView):
	model = Release
	context_object_name = 'releases'
	template_name = 'release/release_list.html'

	def get_queryset(self):
		return self.request.user.profile.wishlist.all()
