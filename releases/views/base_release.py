from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from releases.models import Release, FavouriteRelease


class BaseRelease(LoginRequiredMixin, ListView):
    context_object_name = "releases"

    template_name = "release/release_list.html"
    model = Release

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        pks = list(FavouriteRelease.objects.values_list('release', flat=True))
        context['fav_releases'] = pks
        return context
