from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.db import transaction

from users.models import Label


class SetAsMainLabelView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Label
    http_method_names = ['post']

    def test_func(self):
        label = self.get_object()

        return label.belongs_to_user(self.request.user)

    def post(self, request, *args, **kwargs):
        new_main_label = self.get_object()

        with transaction.atomic():
            # clear is_main flag on all user's labels
            labels = self.request.user.profile.labels.all()

            for label in labels:
                label.is_main = False

            Label.objects.bulk_update(labels, ['is_main'])

            # set is_main flag on the new main label
            new_main_label.is_main = True
            new_main_label.save()

        messages.success(request, "You've successfully changed your main label.")

        return HttpResponseRedirect(reverse_lazy('users_label_list'))
