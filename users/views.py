from django.shortcuts import render
from django.views.generic import CreateView

from .forms import CustomUserCreationForm


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = '/'

