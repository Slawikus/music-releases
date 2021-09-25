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

    def form_valid(self, form):
        form.instance.is_submitted = True
        form.instance.submitted_at = timezone.datetime.now()
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        return obj.profile == self.request.user.profile

    def post(self, request, *args, **kwargs):
        release = Release.objects.get(pk=kwargs['pk'])
        if None in list(release.__dict__.values()):
            messages.error(request, "all fields must filled")
            return HttpResponseRedirect(reverse_lazy('my_releases'))
