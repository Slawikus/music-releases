import factory
from django.db.models.signals import post_save
from users.models import User, Profile, Label


@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")
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
