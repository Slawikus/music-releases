from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.db import IntegrityError

from labels.forms import LabelForm
from users.models import Label


class CreateLabelView(CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'label/label_add.html'
    success_url = reverse_lazy('users_label_list')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        try:
            return super().form_valid(form)
        except IntegrityError:
            form.add_error('name', "You already have this label")
            return super().form_invalid(form)