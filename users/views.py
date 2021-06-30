from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import IntegrityError

from .forms import CustomUserCreationForm, EditProfileForm
from .models import Profile, ProfileCurrency


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = '/'


class EditProfileView(UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('profile_edit')

    def get_object(self, queryset=None):
        return self.request.user.profile


class CreateCurrencyView(CreateView):
    model = ProfileCurrency
    fields = ['currency']
    template_name = 'currencies_list.html'
    success_url = reverse_lazy('currencies_create')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        try:
            return super().form_valid(form)
        except IntegrityError:
            form.add_error('currency', 'You have already chosen that currency')
            return self.form_invalid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(CreateCurrencyView, self).get_context_data(**kwargs)
        context['currencies_list'] = ProfileCurrency.objects.filter(profile=self.request.user.profile)
        return context


class DeleteCurrencyView(DeleteView):
    model = ProfileCurrency
    success_url = reverse_lazy('currencies_create')
