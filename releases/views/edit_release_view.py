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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        release = self.get_object()
        context["percent"] = self.find_completeness_percent(release)
        return context

    def find_completeness_percent(self, release):
        empty_fields_amount = len([i for i in release.__dict__.values() if i is None])
        all_fields_amount = len(release.__dict__)
        percent = (all_fields_amount - empty_fields_amount) / all_fields_amount * 100
        return percent

    def test_func(self):
        obj = self.get_object()
        return obj.profile == self.request.user.profile
