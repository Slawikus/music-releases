from django.db import models
from django_countries.fields import CountryField
import uuid
from .invitation import Invitation


class Profile(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    country = CountryField()
    address = models.TextField(blank=True, null=True)
    submission_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    trade_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=True  # TODO: make this False
    )

    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        super(Profile, self).save(*args, **kwargs)
        if is_new:
            for _ in range(3):
                Invitation.objects.create(profile=self.user.profile)
