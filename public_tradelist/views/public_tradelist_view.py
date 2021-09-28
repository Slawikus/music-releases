from django.views.generic import FormView
from django.shortcuts import get_object_or_404
from releases.models import Release
from users.models import Profile
from django.contrib import messages
from public_tradelist.models import TradeRequestItem, create_trade_request_item
from public_tradelist.forms import TradeListForm


# Create your views here.
class PublicTradeListView(FormView):
    template_name = "tradelist.html"
    form_class = TradeListForm
    success_url = "/"

    def form_valid(self, form):

        form.instance.profile = get_object_or_404(Profile, trade_id=self.kwargs["trade_id"])

        create_trade_request_item(self, form)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        profile = get_object_or_404(Profile, trade_id=self.kwargs['trade_id'])
        context = super().get_context_data()
        context["title"] = "Public Tradelist"
        context["releases"] = Release.objects.tradelist_items_for_profile(profile)

        return context
