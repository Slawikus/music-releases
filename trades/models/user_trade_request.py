from django.db import models
from users.models import Profile


class UserTradeRequest(models.Model):
    name = models.CharField(max_length=255)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="users_trade_requests")
    created = models.DateTimeField(auto_now_add=True)
    from_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="sent_trade_requests",
        null=True
    )
