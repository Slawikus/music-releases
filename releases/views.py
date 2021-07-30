from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from .forms import CreateReleaseForm
from .models import Release

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


class AllReleaseView(ListView):

    template_name = "release_list.html"
    model = Release

class UpcomingReleasesView(AllReleaseView):

    def get_queryset(self):
        return Release.objects.filter(release_date__gte=date.today())

class RecentlyReleasedView(AllReleaseView):

    def get_queryset(self):
        return Release.objects.filter(release_date__lte=date.today())