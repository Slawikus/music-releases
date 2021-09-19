from django.db import models
from django.core.validators import FileExtensionValidator
from phonenumber_field.modelfields import PhoneNumberField
from configuration.file_storage import DuplicationFixFileSystemStorage
from users.models import Profile
# Create your models here.


class BandSubmission(models.Model):
    name = models.CharField(max_length=255)
    album = models.FileField(
        upload_to='band_submissions/files/',
        validators=[FileExtensionValidator(['zip', 'rar'])],
        help_text='upload zip or rar file containing your album samples',
        storage=DuplicationFixFileSystemStorage()
    )
    best_track = models.FileField(
        upload_to='band_submissions/audio/',
        validators=[FileExtensionValidator(['mp3'])],
        verbose_name='best track',
        storage=DuplicationFixFileSystemStorage()
    )

    front_cover = models.ImageField(
        upload_to='band_submissions/image/',
        verbose_name='front cover',
        blank=True,
        null=True,
        storage=DuplicationFixFileSystemStorage()
    )
    email = models.EmailField()
    phone_number = PhoneNumberField()

    biography = models.TextField(
        help_text="Write about releases, press mention or tour dates"
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='submissions')
