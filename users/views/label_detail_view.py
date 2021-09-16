from django.views.generic import DetailView
from users.models import Label


class LabelDetailView(DetailView):
	context_object_name = "label"
	model = Label
	template_name = "label/label_detail.html"
