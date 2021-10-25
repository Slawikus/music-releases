import json

from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from releases.models import Release
from release_collections.models import ReleaseCollection



class CollectionCreateView(LoginRequiredMixin, View):
	def get(self, request):
		releases = Release.submitted.all()
		return render(request, "collection/collection_create.html", {"releases": releases})

	def post(self, request):
		post_data = request.POST
		release_ids = json.loads(post_data['release_ids'])["all"]

		if not self.check_if_release_ids_exists(release_ids):
			return HttpResponse("do not try to use wrong releases")

		ReleaseCollection.objects.create(
			profile=request.user.profile,
			name=post_data['collection_name'],
			release_ids=release_ids
		)

		return HttpResponseRedirect(reverse("collection_list"))

	def check_if_release_ids_exists(self, release_ids):
		real_release_ids = Release.submitted.values_list("pk", flat=True)
		for release_id in release_ids:
			if not release_id in real_release_ids:
				return False
		return True
