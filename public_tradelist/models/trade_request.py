from django.db import models
from users.models import Profile
from notifications.models import Notification
from django.urls import reverse


# Create your models here.
class TradeRequest(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="trade_requests")
    created = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        is_new = self.id is None
        super().save(force_insert, force_update)

        if is_new:
            Notification.objects.create(
                profile=self.profile,
                message=f"trade request from {self.name}",
                target_url=reverse("trade_details", args=[self.id])
            )
