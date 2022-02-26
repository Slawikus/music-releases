from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.utils import timezone

from releases.models import Release
from releases.filters import ReleaseFilter


class UpcomingReleasesView(LoginRequiredMixin, ListView):
    template_name = "release/upcoming.html"
    model = Release
    context_object_name = "releases"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = ReleaseFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        return super().get_queryset().filter(is_submitted=True,
                                             release_date__gte=timezone.now(),
                                             ).order_by("-submitted_at")
