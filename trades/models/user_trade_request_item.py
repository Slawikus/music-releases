from django.db import models
from releases.models import Release
from trades.models import UserTradeRequest


class UserTradeRequestItem(models.Model):
    trade_request = models.ForeignKey(UserTradeRequest, on_delete=models.CASCADE, related_name="user_trade_items")
    release = models.ForeignKey(Release, on_delete=models.CASCADE, related_name="user_trade_items")
    band_name = models.CharField(
        max_length=250,
        verbose_name='Band name(s)',
    )
    release_date = models.DateField(
        verbose_name='Release date',
    )
    trade_points = models.DecimalField(
        decimal_places=1,
        max_digits=3,
    )

    prices_with_currencies = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
