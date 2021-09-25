from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import  UpdateView
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

    def post(self, request, *args, **kwargs):
        release = Release.objects.get(pk=kwargs['pk'])
        _fields_dict = release.__dict__

        # exclude fields that may be empty
        del _fields_dict['submitted_at']
        del _fields_dict['media_format_details']
        del _fields_dict['limited_edition']

        fields_values = list(_fields_dict.values())

        if None in fields_values:
            empty_fields = [i for i in _fields_dict.keys() if _fields_dict[i] is None]
            messages.error(request, "%s fields must filled" % ", ".join(empty_fields))
            return HttpResponseRedirect(reverse_lazy('my_releases'))

        else:

            release.is_submitted = True
            release.submitted_at = timezone.datetime.now()
            release.save()

            messages.success(request, "successfully submitted!")
            return HttpResponseRedirect(reverse_lazy('my_releases'))
