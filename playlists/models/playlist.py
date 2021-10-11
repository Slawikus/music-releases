from django.db import models
from users.models import Profile


class Playlist(models.Model):
	name = models.CharField(max_length=255, unique=True)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	date = models.DateField(auto_now_add=True)

	def __str__(self):
		return f"{self.profile.user.name} - {self.name}"
