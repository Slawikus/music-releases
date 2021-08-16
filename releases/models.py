from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django_countries.fields import CountryField

from users.models import Profile, Label, ProfileCurrency


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

    submitted_at = models.DateTimeField(
        verbose_name="submitted date",
        blank=True,
        null=True
    )

    label = models.ForeignKey(
        Label,
        on_delete=models.CASCADE,
        related_name='release',
    )

    class BaseStyle(models.TextChoices):
        BLACK_METAL = 'black_metal', 'Black Metal'
        DEATH_METAL = 'death_metal', 'Death Metal'
        TRASH_METAL = 'trash_metal', 'Thrash Metal'

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

    is_submitted = models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        is_new = self.id is None
        super().save(force_insert, force_update)
        if is_new:
            WholesaleAndTrades.objects.create(release=self, id=self.id)

    def divide_media_format(self):
        return " | ".join(self.media_format_details.split(", "))

    def currencies_without_price(self, profile):
        profile_currencies = ProfileCurrency.objects.filter(profile=profile)
        release_currencies_ids = ReleaseWholesalePrice.objects.filter(release=self).values_list('currency', flat=True)
        release_currencies = ProfileCurrency.objects.filter(id__in=release_currencies_ids)
        currency_choices = profile_currencies.exclude(id__in=release_currencies)

        return currency_choices


class WholesaleAndTrades(models.Model):
    YES_NO_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )

    release = models.OneToOneField(Release, on_delete=models.CASCADE)
    available_for_trade = models.BooleanField(default=False, choices=YES_NO_CHOICES)
    trade_points = models.DecimalField(
        decimal_places=1,
        max_digits=3,
        validators=[MinValueValidator(0), MaxValueValidator(30)],
        null=True,
        blank=True
    )
    trade_remarks = models.CharField(max_length=250, null=True, blank=True)
    available_for_wholesale = models.BooleanField(default=False, choices=YES_NO_CHOICES)


class ReleaseWholesalePrice(models.Model):
    release = models.ForeignKey(
        Release,
        related_name='release_price',
        on_delete=models.CASCADE
    )
    currency = models.ForeignKey(
        ProfileCurrency,
        related_name='release_currency',
        on_delete=models.CASCADE,
    )
    price = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['release', 'currency'],
                name='unique_release_per_currency'
            ),
        ]


# Реализую в следующем ПРе
class MarketingInfos(models.Model):
    release = models.OneToOneField(Release, on_delete=models.CASCADE)
    style = models.CharField(max_length=250, null=True, blank=True)
    release_overview = models.TextField(null=True, blank=True)
    youtube_url = models.URLField(null=True, blank=True)
    soundcloud_url = models.URLField(null=True, blank=True)
    press_feedback = models.TextField(null=True, blank=True)
