from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db import IntegrityError

from .forms import CustomUserCreationForm, EditProfileForm, CreateCurrencyForm, LabelForm
from .models import Profile, ProfileCurrency, Label
from releases.models import TradeRequest


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = '/'


class EditProfileView(UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'profile/profile_edit.html'
    success_url = reverse_lazy('profile_edit')

    def get_object(self, queryset=None):
        return self.request.user.profile


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


class ListProfileCurrencyView(ListView):
    model = ProfileCurrency
    template_name = 'profile/currencies_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(profile=self.request.user.profile)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreateCurrencyForm(self.request.user.profile)
        return context


class DeleteProfileCurrencyView(DeleteView):
    model = ProfileCurrency
    success_url = reverse_lazy('currencies_list')


class CreateLabelView(CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'label/label_add.html'
    success_url = reverse_lazy('labels_list')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        try:
            return super().form_valid(form)
        except IntegrityError:
            form.add_error('name', "You already have this label")
            return super().form_invalid(form)


class ListLabelView(ListView):
    model = Label
    context_object_name = 'labels'
    template_name = 'label/labels_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(profile=self.request.user.profile)


class UpdateLabelView(UpdateView):
    model = Label
    context_object_name = 'label'
    template_name = 'label/label_update.html'
    form_class = LabelForm
    success_url = reverse_lazy('labels_list')

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError:
            form.add_error('name', "You already have this label")
            return super().form_invalid(form)


class DeleteLabelView(DeleteView):
    model = Label
    context_object_name = 'label'
    template_name = 'label/label_delete.html'
    success_url = reverse_lazy('labels_list')


class ShowTradeListRequestsView(ListView):
    model = TradeRequest
    template_name = "profile/trade_requests.html"
    context_object_name = "trade_requests"

    def get_queryset(self):
        return TradeRequest.objects.filter(profile=self.request.user.profile)
