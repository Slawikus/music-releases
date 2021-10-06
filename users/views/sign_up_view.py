from django.http import HttpResponse
from django.views.generic import FormView

from users.forms import SignUpForm
from users.models import Invitation
from django.core.exceptions import ObjectDoesNotExist
from users.models import User, Label
from django.contrib.auth import login


class SignUpView(FormView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        try:
            invitation = Invitation.objects.get(public_id=self.kwargs['public_id'])
        except ObjectDoesNotExist:
            return HttpResponse(self.request, "Sorry, your invitation link is not valid", status=200)
        if not invitation.is_active:
            return HttpResponse(self.request,
                                "Sorry, your invitation link is already been used and not valid anymore")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        user = User.objects.create_user(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password1']
        )

        profile = user.profile
        profile.country = form.cleaned_data['country']
        profile.save()

        Label.objects.create(
            profile=profile,
            name=form.cleaned_data['main_label_name'],
            is_main=True
        )

        login(self.request, user)

        invitation = Invitation.objects.get(public_id=self.kwargs['public_id'])
        invitation.is_active = False
        invitation.save()

        return super().form_valid(form)
