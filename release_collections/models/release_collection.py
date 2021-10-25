from django.db import models
from users.models import Profile
from django.contrib.postgres.fields import ArrayField


class ReleaseCollection(models.Model):
	name = models.CharField(max_length=255)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="release_collections")
	release_ids = ArrayField(models.PositiveIntegerField())

	def __str__(self):
		return f"{self.profile.user.name} - {self.name}"
