from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from public_tradelist.models import TradeRequest


class TradeRequestListView(LoginRequiredMixin, ListView):
    model = TradeRequest
    template_name = "profile/trade_requests.html"
    context_object_name = "trade_requests"

    def get_queryset(self):
        return TradeRequest.objects.get(profile=self.request.user.profile)

