from django.views.generic import ListView
from users.models import Invitation


class ShowInvitationsView(ListView):
    model = Invitation
    template_name = "invitation.html"
    context_object_name = "invitations"

    def get_queryset(self):
        return super().get_queryset().filter(profile=self.request.user.profile)
