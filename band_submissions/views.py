from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseForbidden

from .forms import BandSubmissionForm
from .models import BandSubmission
from users.models import Profile
# Create your views here.


class BandSubmissionCreateView(UserPassesTestMixin, CreateView):
    model = BandSubmission
    template_name = "band_submissions/band_submission.html"
    form_class = BandSubmissionForm
    success_url = reverse_lazy("success")

    def test_func(self):
        profile = Profile.objects.filter(submission_uuid=self.kwargs['uuid'])
        return profile.exists()

    def handle_no_permission(self):
        return HttpResponseForbidden(self.request)

    def form_valid(self, form):
        form.instance.profile = Profile.objects.get(submission_uuid=self.kwargs['uuid'])
        return super().form_valid(form)
