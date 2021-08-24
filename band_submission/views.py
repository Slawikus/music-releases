from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.

from .forms import BandSubmissionForm
from .models import BandSubmission
from users.models import Profile
# Create your views here.


class BandSubmissionCreateView(CreateView):
    model = BandSubmission
    template_name = "band_submission.html"
    form_class = BandSubmissionForm
    success_url = reverse_lazy("success")

    def dispatch(self, request, *args, **kwargs):

        return super(BandSubmissionCreateView, self).dispatch(*args, **kwargs)

    def test_func(self):
        return Profile.objects.filter(submission_uuid=self.kwargs['uuid']).exists()

    def get_form_kwargs(self):
        kwargs = super(BandSubmissionCreateView, self).get_form_kwargs()
        return kwargs