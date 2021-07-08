from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver
import pycountry

from configuration.settings import CURRENCY_CHOICES


# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    label_name = models.CharField(max_length=250, blank=True, null=True)
    country = CountryField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.email


class ProfileCurrency(models.Model):

    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
    )

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='currencies',
    )

    def __str__(self):
        return self.get_currency_display()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['currency', 'profile'],
                name='unique_currency_per_profile'
            ),
        ]


class Label(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=250,
        verbose_name='Label name',
        help_text='Label name as you write on your releases',
    )
    logo = models.ImageField(
        upload_to='images/labels/',
        blank=True,
        null=True,
        verbose_name='Label logo',
        help_text='For best result - black logo on white or transparent background',
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Short label description',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'profile'],
                name='unique_label_per_profile'
            ),
        ]


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
