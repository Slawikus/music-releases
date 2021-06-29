from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.db import IntegrityError

from .forms import CustomUserCreationForm, EditProfileForm
from .models import Profile, ProfileCurrency, Label


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = '/'


class EditProfileView(UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('edit_profile')

    def get_object(self, queryset=None):
        return self.request.user.profile


class AddCurrenciesView(CreateView):
    model = ProfileCurrency
    fields = ['currency']
    template_name = 'edit_currencies.html'
    success_url = reverse_lazy('edit_currencies')

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
        context = super(AddCurrenciesView, self).get_context_data(**kwargs)
        context['currencies_list'] = ProfileCurrency.objects.filter(profile=self.request.user.profile)
        return context


class DeleteCurrenciesView(DeleteView):
    model = ProfileCurrency
    template_name = 'delete_currencies.html'
    success_url = reverse_lazy('edit_currencies')


class AddLabelView(CreateView):
    model = Label
    fields = ['name', 'logo', 'description']
    template_name = 'label_add.html'
    success_url = reverse_lazy('label_add')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


class ListLabelsView(ListView):
    model = Label
    template_name = 'labels_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(profile=self.request.user.profile)