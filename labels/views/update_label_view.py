from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.db import IntegrityError

from labels.forms import LabelForm
from users.models import Label


class UpdateLabelView(UpdateView):
    model = Label
    context_object_name = 'label'
    template_name = 'label/label_update.html'
    form_class = LabelForm
    success_url = reverse_lazy('users_label_list')
    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError:
            form.add_error('name', "You already have this label")
            return super().form_invalid(form)
