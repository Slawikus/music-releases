from django.db import models
from users.models import Profile


# Create your models here.
class TradeRequest(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="trade_request")
    created = models.DateTimeField(auto_now_add=True)
