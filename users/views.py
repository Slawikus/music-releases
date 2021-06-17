from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .forms import CustomUserCreationForm, EditProfileForm
from .models import Profile, User


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
        return get_object_or_404(self.model, pk=self.request.user.pk)
