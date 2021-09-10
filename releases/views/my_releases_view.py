from .base_release import BaseRelease


class MyReleasesView(BaseRelease):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "My Releases"
        return context

    def get_queryset(self):
        return super().get_queryset().filter(profile=self.request.user.profile).order_by("-submitted_at")
