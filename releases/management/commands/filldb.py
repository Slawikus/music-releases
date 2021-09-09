from django.core.management.base import BaseCommand
from releases.factories import ReleaseFactory
from users.factories import UserWithProfileFactory


DEFAULT_EMAIL = 'admin@gmail.com'
DEFAULT_PASSWORD = 'admin'


class Command(BaseCommand):
	def handle(self, *args, **options):
		user = UserWithProfileFactory.create(
			email=DEFAULT_EMAIL,
			password=DEFAULT_PASSWORD,
			is_superuser=True
		)

		ReleaseFactory.create_batch(3, is_submitted=True, profile=user.profile)
		ReleaseFactory.create_batch(2, profile=user.profile)
