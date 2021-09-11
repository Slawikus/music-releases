from django.views.generic import DeleteView
from django.urls import reverse_lazy
from users.models import ProfileCurrency


class DeleteProfileCurrencyView(DeleteView):
    model = ProfileCurrency
    success_url = reverse_lazy('currencies_list')