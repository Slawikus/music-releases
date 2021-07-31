from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy

from .forms import CreateReleaseForm
from .models import Release


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
