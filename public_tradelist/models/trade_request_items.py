from django.db import models
from .trade_request import TradeRequest
from releases.models import Release


class TradeRequestItem(models.Model):
    trade_request = models.ForeignKey(TradeRequest, on_delete=models.CASCADE, related_name="trade_items")
    release = models.ForeignKey(Release, on_delete=models.CASCADE, related_name="trade_items")
    quantity = models.PositiveIntegerField()