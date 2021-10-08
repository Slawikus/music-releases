from django.views.generic import DetailView
from releases.models import Release
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ReleaseDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
	model = Release
	context_object_name = "release"
	template_name = "release/release_detail_view.html"

	def test_func(self):
		release = self.get_object()
		if not release.is_submitted:
			if self.request.user.profile != release.profile:
				return False

		return True
