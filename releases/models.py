from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField

from users.models import Profile, Label


def validate_file_size(value):
    filesize = value.size

    if filesize > 1048576:
        raise ValidationError("The maximum file size that can be uploaded is 1MB")
    else:
        return value


class Release(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='release'
    )
    band_name = models.CharField(
        max_length=250,
        verbose_name='Band name(s)',
        help_text='Enter band name here. If split release - add band names with“/“ i.e. Nokturnal Mortum / Drudkh',
    )
    country = CountryField(verbose_name='Band country')
    album_title = models.CharField(
        max_length=250,
        verbose_name='Album title'
    )
    release_date = models.DateField(
        verbose_name='Release date',
        help_text='For past/old releases exact date is not important, feel free just to select January 1st, but with '
                  'correct year. For recent/upcoming releases - please try to set the date exactly. This release will '
                  'be shown in Upcoming Releases section.',
    )
    label = models.ForeignKey(
        Label,
        on_delete=models.CASCADE,
        related_name='release',
    )

    class BaseStyle(models.TextChoices):
        BLACK_METAL = 'BM', 'Black Metal'
        DEATH_METAL = 'DM', 'Death Metal'
        TRASH_METAL = 'TM', 'Thrash Metal'

    base_style = models.CharField(
        max_length=250,
        choices=BaseStyle.choices,
    )
    cover_image = models.ImageField(
        upload_to='images/covers/',
        verbose_name='Front cover image',
        help_text='Select image with minimum size of 800x800 pixel'
    )

    class Formats(models.TextChoices):
        CD = 'CD', 'CD'
        VINYL = 'Vinyl', 'Vinyl'
        TAPE = 'Tape', 'Tape'
        DVD = 'DVD', 'DVD'

    format = models.CharField(
        max_length=5,
        choices=Formats.choices,
        default='CD'
    )
    sample = models.FileField(
        upload_to='audios/releases/',
        validators=[validate_file_size, FileExtensionValidator(['mp3'])],
        help_text='Upload up to 1 minute sample of the album to give fellow label owners a taste of this release'
    )
    media_format_details = models.CharField(
        max_length=250,
        help_text='E.g. Digipak, 2xGatefold etc.',
        blank=True,
        null=True,
    )
    limited_edition = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    is_published = models.BooleanField(default=False)

    def get_absolute_url(self, *args, **kwargs):
        return reverse('release_detail', kwargs={'pk': self.pk})
