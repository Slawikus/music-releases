from .invitation import Invitation
from labels.models import Label
from .profile import Profile
from .profile_currency import ProfileCurrency
from .user import User
from .user_manager import UserManager
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


__all__ = [
	Invitation,
	Label,
	Profile,
	ProfileCurrency,
	User,
	UserManager,
	create_or_update_user_profile
]