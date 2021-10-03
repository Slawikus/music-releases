import factory
from public_tradelist.models import TradeRequestItem
from public_tradelist.factories import TradeRequestFactory
from releases.factories import ReleaseFactory
from random import randint


class TradeRequestItemFactory(factory.django.DjangoModelFactory):
	trade_request = factory.SubFactory(TradeRequestFactory)
	release = factory.SubFactory(ReleaseFactory)
	quantity = randint(1, 5)

	class Meta:
		model = TradeRequestItem