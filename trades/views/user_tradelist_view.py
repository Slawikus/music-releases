from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404

from releases.models import Release
from trades.forms.user_tradelist_form import UserTradeListForm
from trades.models import UserTradeRequest, create_trade_request_item
from users.models import Profile
from django.contrib import messages


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
        form.instance.name = self.request.user.profile.label_name

        create_trade_request_item(self, form)

        messages.success(self.request, 'The trade request has been sent')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        profile = self.other_profile
        context = super().get_context_data()
        context["title"] = "Tradelist"
        context["releases"] = Release.objects.tradelist_items_for_profile(profile)
        context["label_name"] = profile.label_name

        return context
