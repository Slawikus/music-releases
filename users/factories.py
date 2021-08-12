import factory
from users.models import User, Profile
from django.db.models.signals import post_save
from .models import Label


# more about using profile and user models in factory boy here
# https://factoryboy.readthedocs.io/en/stable/recipes.html#:~:text=class%20ProfileFactory(factory.django.DjangoModelFactory)%3A
@factory.django.mute_signals(post_save)
class ProfileFactory(factory.django.DjangoModelFactory):

    user = factory.SubFactory("releases.factories.UserFactory", profile=None)

    class Meta:
        model = Profile


@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):

    profile = factory.RelatedFactory(ProfileFactory, factory_related_name='user')
    email = factory.Faker("email")
    password = factory.Faker("password")
    username = factory.Faker("name")

    class Meta:
        model = User




class LabelFactory(factory.django.DjangoModelFactory):

    profile = factory.SubFactory(ProfileFactory)
    name = factory.Faker("name")

    class Meta:
        model = Label