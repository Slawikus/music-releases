from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from releases.factories import ReleaseFactory
from users.factories import UserWithProfileFactory
from labels.factories import LabelFactory
from band_submissions.factories import BandSubmissionFactory
from public_tradelist.factories import TradeRequestFactory
from random import randint


DEFAULT_EMAIL = 'admin@gmail.com'
DEFAULT_PASSWORD = 'admin'


class Command(BaseCommand):
	def handle(self, *args, **options):
		user = UserWithProfileFactory.create(
			email=DEFAULT_EMAIL,
			password=make_password(DEFAULT_PASSWORD),
			is_superuser=True
		)

		users_label = LabelFactory.create(profile=user.profile)
		ReleaseFactory.create_batch(50, label=users_label)

		labels = LabelFactory.create_batch(200)
		for label in labels:
			ReleaseFactory.create_batch(randint(2, 50), label=label)
			TradeRequestFactory.create_batch(randint(3, 10), profile=label.profile)

		BandSubmissionFactory.create_batch(50)
		BandSubmissionFactory.create_batch(50, profile=user.profile)
		TradeRequestFactory.create_batch(10, profile=user.profile)
