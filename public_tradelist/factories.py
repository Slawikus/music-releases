import factory
from users.factories import ProfileFactory
from .models import TradeRequest, TradeRequestItem
from releases.factories import ReleaseFactory
from random import randint


class TradeRequestFactory(factory.django.DjangoModelFactory):
	name = factory.Faker("name")
	email = factory.Faker("email")
	profile = factory.SubFactory(ProfileFactory)

	class Meta:
		model = TradeRequest


class TradeRequestItemFactory(factory.django.DjangoModelFactory):
	trade_request = factory.SubFactory(TradeRequestFactory)
	release = factory.SubFactory(ReleaseFactory)
	quantity = randint(1, 5)

	class Meta:
		model = TradeRequestItem
