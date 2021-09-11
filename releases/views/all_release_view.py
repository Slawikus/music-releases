from .base_release import BaseRelease
from releases.models import Release

class AllReleaseView(BaseRelease):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "All Releases"
        return context

    def get_queryset(self):
        return Release.objects.filter(is_submitted=True)

