from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from public_tradelist.models import TradeRequest
from trades.models import UserTradeRequest


class TradeRequestListView(LoginRequiredMixin, ListView):
    model = TradeRequest
    template_name = "profile/trade_requests.html"
    context_object_name = "trade_requests"

    def get_queryset(self):
        return TradeRequest.objects.filter(profile=self.request.user.profile)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TradeRequestListView, self).get_context_data(**kwargs)
        context['users_trade_requests'] = UserTradeRequest.objects.filter(profile=self.request.user.profile)

        return context
