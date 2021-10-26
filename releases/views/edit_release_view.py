from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from releases.forms import UpdateReleaseForm
from releases.models import Release

class EditReleaseView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Release
    form_class = UpdateReleaseForm
    template_name = "release/edit_release.html"
    success_url = reverse_lazy("my_releases")

    def test_func(self):
        obj = self.get_object()
        return obj.profile == self.request.user.profile
