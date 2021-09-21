from django.views.generic import ListView
from users.models import Label


class ListLabelView(ListView):
    model = Label
    context_object_name = 'labels'
    template_name = 'label/labels_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(profile=self.request.user.profile)
