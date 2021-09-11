from django.views.generic import UpdateView
from django.urls import reverse_lazy
from users.forms import EditProfileForm
from users.models import Profile


class EditProfileView(UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('profile_edit')
    def get_object(self, queryset=None):
        return self.request.user.profile