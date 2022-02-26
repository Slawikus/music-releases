from django.db import models
from .trade_request import TradeRequest
from releases.models import Release
from django.core.validators import ValidationError


def create_trade_request(form, trade_item_model, profile):
    items = form.cleaned_data["items"]

    trade_request = form.save(commit=True)
    releases = Release.objects.tradelist_items_for_profile(profile)

    for pair in items.split(","):

        release_id, quantity = pair.split(":")

        if not releases.filter(id=release_id).exists():
            trade_request.delete()
            raise ValidationError("Do not try to use wrong release")

        release = Release.objects.get(id=release_id)
        prices_with_currencies = " ".join(
            [f"{currency.currency} {currency.price}" for currency in release.wholesale_prices.all()])

        trade_item_model.objects.create(trade_request=trade_request,
                                        release=release,
                                        quantity=quantity,
                                        band_name=release.band_name,
                                        release_date=release.release_date,
                                        trade_points=release.releasetradesinfo.trade_points,
                                        prices_with_currencies=prices_with_currencies,
                                        )


class TradeRequestItem(models.Model):
    trade_request = models.ForeignKey(TradeRequest, on_delete=models.CASCADE, related_name="trade_items")
    release = models.ForeignKey(Release, on_delete=models.CASCADE, related_name="trade_items")
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
        null=True
    )

    prices_with_currencies = models.CharField(max_length=255)

    quantity = models.PositiveIntegerField()
