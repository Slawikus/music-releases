from django.views.generic import CreateView
from .forms import BandSubmissionForm
from django.urls import reverse_lazy
# Create your views here.


class BandSubmissionView(CreateView):

    template_name = "band_submission.html"
    form_class = BandSubmissionForm
    success_url = reverse_lazy("success")