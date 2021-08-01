from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy, reverse
from .forms import CreateReleaseForm
from .models import Release
from .filters import ReleaseFilter

from datetime import date


class CreateReleaseView(LoginRequiredMixin, CreateView):
    model = Release
    template_name = 'release_add.html'
    form_class = CreateReleaseForm
    login_url = 'login'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['profile'] = self.request.user.profile
        return kwargs


class SubmitReleaseView(UpdateView):
    model = Release
    fields = ['is_published']

    def get_success_url(self):
        return reverse('release_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.is_published = True
        return super().form_valid(form)


class BaseRelease(ListView):

    context_object_name = "releases"

    template_name = "release_list.html"
    model = Release


class AllReleaseView(BaseRelease):

    def get_queryset(self):
        return Release.objects.filter(is_published=True)


class UpcomingReleasesView(ListView, LoginRequiredMixin):

    template_name = "upcoming.html"
    model = Release

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = ReleaseFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        return super().get_queryset().filter(is_published=True,
                                             release_date__gte=date.today(),
                                             ).order_by("-published_date")


class RecentlySubmittedView(BaseRelease):

    def get_queryset(self):
        return super().get_queryset().filter(is_published=True,
                                             release_date__lte=date.today(),
                                             ).order_by("-published_date")


class MyReleasesView(BaseRelease):

    def get_queryset(self):
        return super().get_queryset().filter(profile=self.request.user.profile).order_by("-release_date")


def publish_release(request, pk):
    release = Release.objects.get(pk=pk)
    release.is_published = True
    release.published_date = date.today()
    release.save()

    return HttpResponseRedirect(reverse("recently_added"))
