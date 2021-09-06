from django.core.management.base import BaseCommand
from releases.factories import ReleaseFactory


class Command(BaseCommand):
	def handle(self, *args, **options):
		ReleaseFactory.create_batch(5, is_submitted=True)
