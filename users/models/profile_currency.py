from django.db import models
from configuration.settings import CURRENCY_CHOICES


class ProfileCurrency(models.Model):
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
    )
    profile = models.ForeignKey(
        "users.Profile",
        on_delete=models.CASCADE,
        related_name='currencies',
    )

    def __str__(self):
        return self.get_currency_display()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['currency', 'profile'],
                name='unique_currency_per_profile'
            ),
        ]
