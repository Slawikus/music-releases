from django.db import models
from users.models import Profile
from django.contrib.postgres.fields import ArrayField


class Playlist(models.Model):
	name = models.CharField(max_length=255, unique=True)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="playlists")
	release_ids = ArrayField(models.PositiveIntegerField())
	date = models.DateField(auto_now_add=True)

	def __str__(self):
		return f"{self.profile.user.name} - {self.name}"
