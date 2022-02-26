from django.urls import reverse_lazy
from django.views.generic import FormView
from django.shortcuts import get_object_or_404
from releases.models import Release
from users.models import Profile
from public_tradelist.models import TradeRequestItem, create_trade_request
from public_tradelist.forms import TradeListForm
from django.core.validators import ValidationError


class PublicTradeListView(FormView):
    template_name = "public_tradelist.html"
    form_class = TradeListForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):

        form.instance.profile = get_object_or_404(Profile, trade_id=self.kwargs["trade_id"])
        trade_owner_profile = get_object_or_404(Profile, trade_id=self.kwargs['trade_id'])
        try:
            create_trade_request(
                form=form,
                trade_item_model=TradeRequestItem,
                profile=trade_owner_profile
            )
            return super().form_valid(form)
        except ValidationError:
            return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        profile = get_object_or_404(Profile, trade_id=self.kwargs['trade_id'])
        context = super().get_context_data()
        context["title"] = "Public Tradelist"
        context["releases"] = Release.objects.tradelist_items_for_profile(profile)

        return context
