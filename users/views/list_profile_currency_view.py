from django.views.generic import ListView
from users.forms import CreateCurrencyForm
from users.models import ProfileCurrency


class ListProfileCurrencyView(ListView):
    model = ProfileCurrency
    template_name = 'currencies_list.html'
    def get_queryset(self):
        return super().get_queryset().filter(profile=self.request.user.profile)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreateCurrencyForm(self.request.user.profile)
        return context
