from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from public_tradelist.models import TradeRequest


class TradeRequestDetailView(LoginRequiredMixin, DetailView):
    model = TradeRequest
    template_name = "profile/trade_request_detail.html"
    context_object_name = "trade_request"
