from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from releases.factories import ReleaseFactory
from users.factories import UserWithProfileFactory
from labels.factories import LabelFactory

DEFAULT_EMAIL = 'admin@gmail.com'
DEFAULT_PASSWORD = 'admin'


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = UserWithProfileFactory.create(
            email=DEFAULT_EMAIL,
            password=make_password(DEFAULT_PASSWORD),
            is_superuser=True
        )

        label = LabelFactory.create(name='Metal Blade Records', profile=user.profile, is_main=True)

        ReleaseFactory.create_batch(3, is_submitted=True, profile=user.profile, label=label)
        ReleaseFactory.create_batch(2, profile=user.profile, label=label)
