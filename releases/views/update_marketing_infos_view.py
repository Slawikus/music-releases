from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.views.generic import UpdateView
from django.urls import reverse_lazy, reverse

from releases.forms import UpdateMarketingInfosForm
from releases.models import Release, MarketingInfos


class UpdateMarketingInfosView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MarketingInfos
    form_class = UpdateMarketingInfosForm
    template_name = 'release/marketing_infos_edit.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        self.release = get_object_or_404(Release, pk=self.kwargs.get("pk"))
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('marketing_infos_edit', args=[self.release.pk])

    def test_func(self):
        obj = self.get_object()
        return obj.release.profile == self.request.user.profile

    def get_object(self, queryset=None):
        return self.release.marketinginfos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['release'] = self.release
        return context
