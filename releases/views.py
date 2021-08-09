from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, ListView
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse_lazy, reverse
from django.contrib import messages

from django.core.exceptions import ObjectDoesNotExist

from .forms import CreateReleaseForm
from .models import Release
from .filters import ReleaseFilter

from django.utils.timezone import datetime


class CreateReleaseView(LoginRequiredMixin, CreateView):
    model = Release
    template_name = 'release_add.html'
    form_class = CreateReleaseForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['profile'] = self.request.user.profile
        return kwargs


@login_required
def submit_release(request, pk):

    if request.method == "POST":
        release = Release.objects.filter(pk=pk)

        if release.exists():

            if release.profile == request.user.profile:
                if not release.is_submitted:
                    release.is_submitted = True
                    release.submitted_at = datetime.today()
                    release.save()
                else:
                    messages.error(request, "release is already submitted")

            else:
                messages.error(request, "You can't submit someone else's record")

        else:
            messages.error(request, "Release does not exist")

        return HttpResponseRedirect(reverse("my_releases"))

    else:
        return HttpResponseForbidden


class EditReleaseView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    def test_func(self):
        obj = self.get_object()
        return obj.profile == self.request.user.profile

    model = Release

    fields = ['band_name', 'album_title', 'cover_image', 'sample', 'limited_edition']
    template_name = "edit_release.html"
    success_url = reverse_lazy("my_releases")


class BaseRelease(LoginRequiredMixin, ListView):
    context_object_name = "releases"

    template_name = "release_list.html"
    model = Release


class AllReleaseView(BaseRelease):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "All Releases"
        return context

    def get_queryset(self):
        return Release.objects.filter(is_submitted=True)


class UpcomingReleasesView(LoginRequiredMixin, ListView):
    template_name = "upcoming.html"
    model = Release

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = ReleaseFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        return super().get_queryset().filter(is_submitted=True,
                                             submitted_at__gte=datetime.today(),
                                             ).order_by("-submitted_at")


class RecentlySubmittedView(BaseRelease):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Recently Submitted Releases"
        return context

    def get_queryset(self):
        return super().get_queryset().filter(is_submitted=True,
                                             submitted_at__lte=datetime.today(),
                                             ).order_by("-submitted_at")


class MyReleasesView(BaseRelease):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "My Releases"
        return context

    def get_queryset(self):
        return super().get_queryset().filter(profile=self.request.user.profile).order_by("-submitted_at")
