from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy

from .forms import CreateReleaseForm
from .models import Release


# Create your views here.
class CreateReleaseView(CreateView):
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
