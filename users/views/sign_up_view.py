from django.http import HttpResponse
from django.views.generic import FormView

from users.forms import UserProfileCreationForm
from users.models import Invitation
from django.core.exceptions import ObjectDoesNotExist
from users.models import User, Profile, Label
from django.contrib.auth import login


class SignUpView(FormView):
    form_class = UserProfileCreationForm
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

        user = User.objects.create(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password1']
        )

        profile = Profile.objects.get(user=user)
        profile.country = form.cleaned_data['country']
        profile.save()

        Label.objects.create(
            profile=profile,
            name=form.cleaned_data['label_name'],
            is_main=True
        )

        login(self.request, user)

        invitation = Invitation.objects.get(public_id=self.kwargs['public_id'])
        invitation.is_active = False
        invitation.save()


        return super().form_valid(form)
