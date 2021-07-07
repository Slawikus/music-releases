from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db import IntegrityError

from .forms import CustomUserCreationForm, EditProfileForm, CreateCurrencyForm
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


class ListCurrenciesView(ListView):
    model = ProfileCurrency
    template_name = 'currencies_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(profile=self.request.user.profile)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreateCurrencyForm(self.request.user.profile)
        return context


class DeleteCurrencyView(DeleteView):
    model = ProfileCurrency
    success_url = reverse_lazy('currencies_list')
