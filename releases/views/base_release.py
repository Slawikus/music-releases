from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from releases.models import Release

class BaseRelease(LoginRequiredMixin, ListView):
    context_object_name = "releases"
    paginate_by = 20
    template_name = "release/release_list.html"
    model = Release
