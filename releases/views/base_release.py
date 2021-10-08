from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from releases.models import Release


class BaseRelease(LoginRequiredMixin, ListView):
    context_object_name = "releases"
    paginate_by = 20
    template_name = "release/release_list.html"
    model = Release

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wished_ids'] = list(self.request.user.profile.wishlist.values_list("id", flat=True))
        return context
