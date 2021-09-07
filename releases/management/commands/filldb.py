from django.core.management.base import BaseCommand
from releases.factories import ReleaseFactory
from users.models import User


DEFAULT_EMAIL = 'admin@gmail.com'
DEFAULT_PASSWORD = 'admin'


class Command(BaseCommand):
	def handle(self, *args, **options):
		user = User.objects.create(email=DEFAULT_EMAIL,
								   password=DEFAULT_PASSWORD,
								   is_superuser=True
								   )

		ReleaseFactory.create_batch(5, is_submitted=True, profile=user.profile)
