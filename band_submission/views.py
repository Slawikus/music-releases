from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin

from .forms import BandSubmissionForm
from .models import BandSubmission, BandSubmissionLink
# Create your views here.


class BandSubmissionView(UserPassesTestMixin, CreateView):
    model = BandSubmission
    template_name = "band_submission.html"
    form_class = BandSubmissionForm
    success_url = reverse_lazy("success")

    def test_func(self):
        return BandSubmissionLink.objects.filter(slug=self.kwargs['slug']).exists()

    def form_valid(self, form):
        valid = super().form_valid(form)
        BandSubmissionLink.objects.get(slug=self.kwargs['slug']).delete()

        return valid