from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404

from public_tradelist.views import PublicTradeListView
from releases.models import Release
from users.models import Profile
from django.contrib import messages
from public_tradelist.models import TradeRequest


class CreateTradeRequestView(LoginRequiredMixin, PublicTradeListView, CreateView):
    model = TradeRequest
    fields = ['name']
    form_class = None
    template_name = 'tradelist.html'
    success_url = reverse_lazy('all_releases')

    def dispatch(self, request, *args, **kwargs):
        self.other_profile = get_object_or_404(Profile, pk=self.kwargs.get("pk"))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        form.instance.profile = self.other_profile
        form.instance.profile_requester = self.request.user.profile
        messages.success(self.request, 'The trade request has been sent')

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        profile = self.other_profile
        context["title"] = "Trade Request"
        context["releases"] = Release.objects.tradelist_items_for_profile(profile)

        return context
