from django.db import models
from releases.models import Release
from .playlist import Playlist

class PlaylistItem(models.Model):
	release = models.ForeignKey(Release, on_delete=models.CASCADE, related_name="playlist_items")
	order = models.PositiveIntegerField()
	playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name="items")
