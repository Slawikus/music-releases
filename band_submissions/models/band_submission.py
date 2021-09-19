from django.db import models
from django.core.validators import FileExtensionValidator
from phonenumber_field.modelfields import PhoneNumberField
from users.models import Profile
from configuration.storage import MediaFileSystemStorage
# Create your models here.


class BandSubmission(models.Model):
    name = models.CharField(max_length=255)
    album = models.FileField(
        upload_to='band_submissions/files/',
        validators=[FileExtensionValidator(['zip', 'rar'])],
        help_text='upload zip or rar file containing your album samples',
        storage=MediaFileSystemStorage()
    )
    best_track = models.FileField(
        upload_to='band_submissions/audio/',
        validators=[FileExtensionValidator(['mp3'])],
        verbose_name='best track',
        storage=MediaFileSystemStorage()
    )

    front_cover = models.ImageField(
        upload_to='band_submissions/image/',
        verbose_name='front cover',
        blank=True,
        null=True,
        storage=MediaFileSystemStorage()
    )
    email = models.EmailField()
    phone_number = PhoneNumberField()

    biography = models.TextField(
        help_text="Write about releases, press mention or tour dates"
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='submissions')
