from django.urls import path
from .views import BandSubmissionCreateView
from django.views.generic import TemplateView

urlpatterns = [
    path("create/<uuid:uuid>/", BandSubmissionCreateView.as_view(), name='band_submission'),
    path("success/", TemplateView.as_view(template_name="band_submissions/submission_success.html"), name="success")
]
