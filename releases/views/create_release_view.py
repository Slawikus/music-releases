from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy

from releases.forms import CreateReleaseForm
from releases.models import Release


class CreateReleaseView(LoginRequiredMixin, CreateView):
    model = Release
    template_name = 'release/release_add.html'
    form_class = CreateReleaseForm
    success_url = reverse_lazy('my_releases')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['profile'] = self.request.user.profile
        return kwargs
