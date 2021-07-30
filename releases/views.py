from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy, reverse

from .forms import CreateReleaseForm
from .models import Release


class CreateReleaseView(LoginRequiredMixin, CreateView):
    model = Release
    template_name = 'release_add.html'
    form_class = CreateReleaseForm
    login_url = 'login'
    # success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse('release_detail', kwargs={'pk': self.object.pk})

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


class DetailReleaseView(DetailView):
    model = Release
    template_name = 'release_detail.html'
