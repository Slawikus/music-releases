from django.db import models
from releases.models import Release
from trades.models import UserTradeRequest


class UserTradeRequestItem(models.Model):
    trade_request = models.ForeignKey(UserTradeRequest, on_delete=models.CASCADE, related_name="user_trade_items")
    release = models.ForeignKey(Release, on_delete=models.CASCADE, related_name="user_trade_items")
    quantity = models.PositiveIntegerField()
