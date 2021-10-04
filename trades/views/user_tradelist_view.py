from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
from django.core.validators import ValidationError

from releases.models import Release
from trades.forms.user_tradelist_form import UserTradeListForm
from trades.models import UserTradeRequest, UserTradeRequestItem
from users.models import Profile
from public_tradelist.models import create_trade_request


class CreateTradeRequestView(LoginRequiredMixin, CreateView):
    model = UserTradeRequest
    form_class = UserTradeListForm
    template_name = 'tradelist.html'
    success_url = reverse_lazy('all_releases')

    def dispatch(self, request, *args, **kwargs):
        self.other_profile = get_object_or_404(Profile, pk=self.kwargs.get("pk"))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.profile = self.other_profile
        form.instance.from_profile = self.request.user.profile
        form.instance.name = self.request.user.profile.main_label_name
        trade_owner_profile = get_object_or_404(Profile, pk=self.kwargs['pk'])

        try:
            create_trade_request(
                form=form,
                trade_item_model=UserTradeRequestItem,
                profile=trade_owner_profile
            )
            return super().form_valid(form)
        except ValidationError:
            return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        profile = self.other_profile
        context = super().get_context_data()
        context["title"] = "Tradelist"
        context["releases"] = Release.objects.tradelist_items_for_profile(profile)
        context["label_name"] = profile.main_label_name

        return context
