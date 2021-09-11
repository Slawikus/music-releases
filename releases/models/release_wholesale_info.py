from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


YES_NO_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )


class ReleaseWholesaleInfo(models.Model):
    release = models.OneToOneField("Release", on_delete=models.CASCADE)
    available_for_wholesale = models.BooleanField(default=False, choices=YES_NO_CHOICES)
