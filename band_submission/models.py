from django.db import models
from django.core.validators import FileExtensionValidator
from users.models import Profile, Label
# Create your models here.


class BandSubmission(models.Model):

    name = models.CharField(max_length=255)
    demo_sample = models.FileField(
        upload_to='audio/releases/',
        validators=[FileExtensionValidator(['mp3'])],
    )
    logo = models.ImageField(
        upload_to='images/covers/',
        verbose_name='band logo',
        blank=True,
        null=True,
    )
    email = models.EmailField()
    biography = models.TextField(
        help_text="Write about releases, press mention or tour dates"
    )


class BandSubmissionLink(models.Model):

    slug = models.SlugField(max_length=255)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
