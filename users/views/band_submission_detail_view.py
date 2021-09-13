from band_submissions.models import BandSubmission
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class BandSubmissionDetailView(LoginRequiredMixin, DetailView):
	model = BandSubmission
	context_object_name = "submission"
	template_name = "band_submissions/submission_detail.html"

