from django.urls import path
from .views import BandSubmissionView
from django.views.generic import TemplateView


urlpatterns = [
    path("submit/", BandSubmissionView.as_view(), name='band_submission'),
    path("success/", TemplateView.as_view(template_name="submission_success.html"), name="success")
]