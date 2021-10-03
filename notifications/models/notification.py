from django.db import models
from users.models import Profile


class Notification(models.Model):
	target_url = models.URLField()
	message = models.CharField(max_length=255)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="notifications")
	is_viewed = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
