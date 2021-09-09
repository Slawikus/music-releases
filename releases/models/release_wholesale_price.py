from django.db import models
from users.models import ProfileCurrency


class ReleaseWholesalePrice(models.Model):
    release = models.ForeignKey(
        "releases.Release",
        related_name='wholesale_prices',
        on_delete=models.CASCADE
    )
    currency = models.ForeignKey(
        ProfileCurrency,
        related_name='wholesale_prices_for_currency',
        on_delete=models.CASCADE,
    )
    price = models.DecimalField(decimal_places=2, max_digits=10)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['release', 'currency'],
                name='unique_price_per_release_and_currency'
            ),
        ]