from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


YES_NO_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )


class ReleaseTradesInfo(models.Model):
    release = models.OneToOneField("Release", on_delete=models.CASCADE)
    available_for_trade = models.BooleanField(default=False, choices=YES_NO_CHOICES)
    trade_points = models.DecimalField(
        decimal_places=1,
        max_digits=3,
        validators=[MinValueValidator(0), MaxValueValidator(30)],
        null=True,
        blank=True
    )
