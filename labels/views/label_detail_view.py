from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import Label


class LabelDetailView(LoginRequiredMixin, DetailView):
    context_object_name = "label"
    model = Label
    template_name = "label/label_detail.html"
