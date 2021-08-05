from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, ListView, View
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from .forms import CreateReleaseForm
from .models import Release
from .filters import ReleaseFilter
from .excel import save_excel_file

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


class SubmitReleaseView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Release
    fields = ['is_submitted']
    login_url = 'login'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.is_submitted = True
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        return obj.profile == self.request.user.profile


class EditReleaseView(UpdateView, LoginRequiredMixin):
    model = Release

    login_url = 'login'
    fields = ['band_name', 'album_title', 'cover_image', 'sample', 'limited_edition']
    template_name = "edit_release.html"
    success_url = reverse_lazy("my_releases")


class BaseRelease(ListView, LoginRequiredMixin):
    login_url = 'login'
    context_object_name = "releases"

    template_name = "release_list.html"
    model = Release


class AllReleaseView(BaseRelease):

    def get_queryset(self):
        return Release.objects.filter(is_submitted=True)


class UpcomingReleasesView(ListView, LoginRequiredMixin):
    template_name = "upcoming.html"
    model = Release

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = ReleaseFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        return super().get_queryset().filter(is_submitted=True,
                                             submitted_at__gte=date.today(),
                                             ).order_by("-submitted_at")


class RecentlySubmittedView(BaseRelease):

    def get_queryset(self):
        return super().get_queryset().filter(is_submitted=True,
                                             submitted_at__lte=date.today(),
                                             ).order_by("-submitted_at")


class MyReleasesView(BaseRelease, LoginRequiredMixin):

    def get_queryset(self):
        return super().get_queryset().filter(profile=self.request.user.profile).order_by("-submitted_at")


class ImportReleasesView(View):

    def get(self, request):
        return render(request, "upload_release.html")

    def post(self, request):
        file = request.FILES.get("excel")

        # try:
        save_excel_file(request, file, request.user.profile)
        # except:
        #
        #     context = {"error": "Wrong excel format. Please write as shown in example"}
        #     return render(request, "upload_release.html", context)

        return HttpResponseRedirect(reverse("my_releases"))
