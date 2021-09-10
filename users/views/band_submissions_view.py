from band_submissions.models import BandSubmission
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


class BandSubmissionsView(LoginRequiredMixin, ListView):
    model = BandSubmission
    template_name = "band_submissions/submission_list.html"
    context_object_name = "submissions"

    def get_queryset(self):
        return BandSubmission.objects.filter(profile=self.request.user.profile)

    def get_context_data(self, **kwargs):
        context = super(BandSubmissionsView, self).get_context_data(**kwargs)
        uuid = self.request.user.profile.submission_uuid
        context["link"] = reverse("band_submission", args=[uuid])
        return context
