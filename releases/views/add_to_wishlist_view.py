from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from releases.models import Release
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


class AddToWishlistView(LoginRequiredMixin, View):
	http_method_names = ['post']

	def post(self, request, pk):
		release = get_object_or_404(Release, pk=pk)
		self.request.user.profile.wishlist.add(release)
		return JsonResponse({"result": "success"})
