from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.contrib import messages

from users.models import Label


class DeleteLabelView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Label
    context_object_name = 'label'
    template_name = 'label/label_delete.html'
    success_url = reverse_lazy('labels_list')

    def test_func(self):
        label = self.get_object()
        return label.belongs_to_user(self.request.user)

    def post(self, request, *args, **kwargs):
        label = self.get_object()

        if label.is_main:
            messages.error(request, "Main label cannot be deleted.")
            return HttpResponseRedirect(reverse_lazy('labels_list'))

        return super().post(request, *args, **kwargs)
