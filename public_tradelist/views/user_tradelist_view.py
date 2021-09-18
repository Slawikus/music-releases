from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404

from public_tradelist.forms import UserTradeListForm
from releases.models import Release
from users.models import Profile
from django.contrib import messages
from public_tradelist.models import TradeRequest, TradeRequestItem


class CreateTradeRequestView(LoginRequiredMixin, CreateView):
    model = TradeRequest
    form_class = UserTradeListForm
    template_name = 'tradelist.html'
    success_url = reverse_lazy('all_releases')

    def dispatch(self, request, *args, **kwargs):
        self.other_profile = get_object_or_404(Profile, pk=self.kwargs.get("pk"))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.profile = self.other_profile
        form.instance.profile_requester = self.request.user.profile

        items = form.cleaned_data["items"]

        trade_request = form.save(commit=True)
        releases = Release.objects.tradelist_items_for_profile(self.request.user.profile)

        for pair in items.split(","):

            release_id, quantity = pair.split(":")

            if not releases.filter(id=release_id).exists():
                messages.error(self.request, "Do not try to use wrong release")

            release = Release.objects.get(id=release_id)
            TradeRequestItem.objects.create(trade_request=trade_request,
                                            release=release,
                                            quantity=quantity)

        messages.success(self.request, 'The trade request has been sent')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        profile = self.other_profile
        context = super().get_context_data()
        context["title"] = "Public Tradelist"
        context["releases"] = Release.objects.tradelist_items_for_profile(profile)

        return context
