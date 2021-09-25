from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import  UpdateView
from django.urls import reverse_lazy
from django.utils import timezone
from releases.models import Release
from django.contrib import messages


class SubmitReleaseView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Release
    fields = ['is_submitted']
    login_url = 'login'
    success_url = reverse_lazy('all_releases')

    def form_valid(self, form):
        form.instance.is_submitted = True
        form.instance.submitted_at = timezone.datetime.now()
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()

        if None in list(obj.__dict__.values()):
            messages.error(self.request, "Please fill all fields")
            return False

        return obj.profile == self.request.user.profile
