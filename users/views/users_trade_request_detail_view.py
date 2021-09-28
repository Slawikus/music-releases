from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from trades.models import UserTradeRequest


class UsersTradeRequestDetailView(LoginRequiredMixin, DetailView):
    model = UserTradeRequest
    template_name = "profile/users_trade_request_detail.html"
    context_object_name = "trade_request"
