from django.views.generic import DeleteView
from django.urls import reverse_lazy
from users.models import Label


class DeleteLabelView(DeleteView):
    model = Label
    context_object_name = 'label'
    template_name = 'label/label_delete.html'
    success_url = reverse_lazy('labels_list')
