from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import Label


class LabelListView(LoginRequiredMixin, ListView):
	model = Label
	context_object_name = "labels"
	template_name = "label/label_list.html"
