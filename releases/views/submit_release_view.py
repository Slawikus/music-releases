from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.utils import timezone
from releases.models import Release
from django.contrib import messages
from django.http import HttpResponseRedirect


class SubmitReleaseView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Release
    fields = ['is_submitted']
    login_url = 'login'
    success_url = reverse_lazy('all_releases')

    def test_func(self):
        obj = self.get_object()
        return obj.profile == self.request.user.profile

    def check_if_empty_fields_exists(self, release):
        _fields_dict = release.__dict__

        # exclude fields that may be empty
        del _fields_dict['submitted_at']
        del _fields_dict['media_format_details']
        del _fields_dict['limited_edition']

        fields_values = list(_fields_dict.values())

        return None in fields_values

    def post(self, request, *args, **kwargs):
        release = Release.objects.get(pk=kwargs['pk'])
        empty_fields_exists = self.check_if_empty_fields_exists(release)

        if not empty_fields_exists:

            release.is_submitted = True
            release.submitted_at = timezone.datetime.now()
            release.save()

            messages.success(request, "successfully submitted!")

        else:
            messages.error(request, "please fill all fields before submit")

        return HttpResponseRedirect(reverse_lazy("my_releases"))
