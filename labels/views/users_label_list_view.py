from django.views.generic import ListView
from users.models import Label


class UsersLabelListView(ListView):
    model = Label
    context_object_name = 'labels'
    template_name = 'label/users_label_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(profile=self.request.user.profile)
