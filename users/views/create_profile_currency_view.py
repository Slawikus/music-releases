from django.contrib import messages
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db import IntegrityError
from users.models import ProfileCurrency


class CreateProfileCurrencyView(CreateView):
    model = ProfileCurrency
    fields = ['currency']
    success_url = reverse_lazy('currencies_list')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        try:
            return super().form_valid(form)
        except IntegrityError:
            messages.error(self.request, 'You have already chosen that currency')
            return redirect('currencies_list')