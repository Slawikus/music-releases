from django.db import models
from users.models import Profile
from releases.models import Release


class FavouriteRelease(models.Model):
	profile = models.ForeignKey(Profile,
								related_name='favourite_releases',
								on_delete=models.CASCADE
								)
	release = models.OneToOneField(Release,
								   related_name='favourite_object',
								   on_delete=models.CASCADE
								)
