import factory
from django.db.models.signals import post_save
from users.models import User, Profile, Label, ProfileCurrency
from factory.fuzzy import FuzzyChoice
import pycountry


@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("email")
    password = factory.Faker("password")

    class Meta:
        model = User


class ProfileFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Profile


class UserWithProfileFactory(UserFactory):
    profile = factory.RelatedFactory(ProfileFactory, factory_related_name='user')


class LabelFactory(factory.django.DjangoModelFactory):
    profile = factory.SubFactory(ProfileFactory)
    name = factory.Faker("name")

    class Meta:
        model = Label


class ProfileCurrencyFactory(factory.django.DjangoModelFactory):
    profile = factory.SubFactory(ProfileFactory)
    currency = FuzzyChoice([currency.alpha_3 for currency in pycountry.currencies])

    class Meta:
        model = ProfileCurrency
