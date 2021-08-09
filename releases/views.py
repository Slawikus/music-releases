from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, ListView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse

from .forms import CreateReleaseForm, ImportReleaseForm
from .models import Release
from .filters import ReleaseFilter
from .excel import save_excel_file
from configuration.settings import MEDIA_ROOT

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


class EditReleaseView(LoginRequiredMixin, UpdateView):
    model = Release

    login_url = 'login'
    fields = ['band_name', 'album_title', 'cover_image', 'sample', 'limited_edition']
    template_name = "edit_release.html"
    success_url = reverse_lazy("my_releases")


class BaseRelease(LoginRequiredMixin, ListView):
    login_url = 'login'
    context_object_name = "releases"

    template_name = "release_list.html"
    model = Release


class AllReleaseView(BaseRelease):

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
                                             submitted_at__gte=date.today(),
                                             ).order_by("-submitted_at")


class RecentlySubmittedView(BaseRelease):

    def get_queryset(self):
        return super().get_queryset().filter(is_submitted=True,
                                             submitted_at__lte=date.today(),
                                             ).order_by("-submitted_at")


class MyReleasesView(BaseRelease):

    def get_queryset(self):
        return super().get_queryset().filter(profile=self.request.user.profile).order_by("-submitted_at")


class ImportReleasesView(LoginRequiredMixin, FormView):

    template_name = "upload_release.html"
    form_class = ImportReleaseForm
    success_url = reverse_lazy("my_releases")

    def form_valid(self, form):
        file = form.cleaned_data.get("file")
        profile = self.request.user.profile
        import_error = save_excel_file(file, profile)
        # if result contains any error
        if import_error:
            messages.error(self.request, import_error)
            return self.render_to_response(
                self.get_context_data(request=self.request, form=form)
            )
        else:
            return super().form_valid(form)

def get_example_excel(request):

    with open(f"{MEDIA_ROOT}/excel/example.xlsx", "rb") as file:
        data = file.read()

    response = HttpResponse(data, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=example.xlsx'
    return response