from django.contrib import messages
from django.db import models

from releases.models import Release
from trades.models import UserTradeRequest


def create_trade_request_item(self, form):
    items = form.cleaned_data["items"]

    trade_request = form.save(commit=True)
    releases = Release.objects.tradelist_items_for_profile(self.request.user.profile)

    for pair in items.split(","):

        release_id, quantity = pair.split(":")

        if not releases.filter(id=release_id).exists():
            messages.error(self.request, "Do not try to use wrong release")

        release = Release.objects.get(id=release_id)
        UserTradeRequestItem.objects.create(trade_request=trade_request,
                                            release=release,
                                            quantity=quantity)


class UserTradeRequestItem(models.Model):
    trade_request = models.ForeignKey(UserTradeRequest, on_delete=models.CASCADE, related_name="user_trade_items")
    release = models.ForeignKey(Release, on_delete=models.CASCADE, related_name="user_trade_items")
    quantity = models.PositiveIntegerField()
