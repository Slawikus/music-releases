from django.http import HttpResponse
from django.views.generic import CreateView

from users.forms import CombinedUserProfileCreationForm
from users.models import Invitation
from django.core.exceptions import ObjectDoesNotExist


class SignUpView(CreateView):
    form_class = CombinedUserProfileCreationForm
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
        return super(SignUpView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        valid = super(SignUpView, self).form_valid(form)
        if valid:
            invitation = Invitation.objects.get(public_id=self.kwargs['public_id'])
            invitation.is_active = False
            invitation.save()
        return valid
