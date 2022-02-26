import factory
from users.factories import ProfileFactory
from public_tradelist.models import TradeRequest


class TradeRequestFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")
    email = factory.Faker("email")
    profile = factory.SubFactory(ProfileFactory)

    class Meta:
        model = TradeRequest
