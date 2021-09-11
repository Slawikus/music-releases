from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.views.generic import UpdateView
from django.urls import reverse

from releases.forms import UpdateReleaseWholesaleInfoForm
from releases.models import ReleaseWholesalePrice, ReleaseWholesaleInfo, Release


class UpdateReleaseWholesaleInfoView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ReleaseWholesaleInfo
    form_class = UpdateReleaseWholesaleInfoForm
    template_name = 'release_wholesale_info_edit.html'
    login_url = 'login'
    context_object_name = 'release_wholesale_info'

    def dispatch(self, request, *args, **kwargs):
        self.release = get_object_or_404(Release, pk=self.kwargs.get("pk"))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        release = self.release
        release_wholesale_prices = ReleaseWholesalePrice.objects.select_related('currency').filter(release=self.release)
        context.update(
            {
                'release_wholesale_prices': release_wholesale_prices,
                'release': release
            }
        )

        return context

    def get_success_url(self):
        return reverse('release_wholesale_info_edit', args=[self.release.pk])

    def test_func(self):
        obj = self.get_object()
        return obj.release.profile == self.request.user.profile

    def get_object(self, queryset=None):
        return self.release.releasewholesaleinfo

