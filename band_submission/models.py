from django.db import models
from django.core.validators import FileExtensionValidator
from users.models import Profile
# Create your models here.


class BandSubmission(models.Model):
    name = models.CharField(max_length=255)
    demo_sample = models.FileField(
        upload_to='band_submissions/audio/',
        validators=[FileExtensionValidator(['mp3', 'zip', 'rar'])],
    )
    front_cover = models.ImageField(
        upload_to='band_submissions/image/',
        verbose_name='front cover',
        blank=True,
        null=True,
    )
    email = models.EmailField()
    biography = models.TextField(
        help_text="Write about releases, press mention or tour dates"
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='submissions')
