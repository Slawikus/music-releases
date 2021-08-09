import factory
from users.models import User, Label, Profile
from .models import Release
import random
from django.db.models.signals import post_save


@factory.django.mute_signals(post_save)
class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory("releases.factories.UserFactory", profile=None)


@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("email")
    password = factory.Faker("password")

    profile = factory.RelatedFactory(ProfileFactory, factory_related_name='user')


class LabelFactory(factory.django.DjangoModelFactory):
    profile = factory.SubFactory(ProfileFactory)
    name = factory.Faker("name")

    class Meta:
        model = Label


class ReleaseFactory(factory.django.DjangoModelFactory):
    profile = factory.SubFactory(ProfileFactory)
    band_name = factory.Faker("name")
    country = factory.Faker("country")
    album_title = factory.Faker("misc")
    release_date = factory.Faker("datetime")
    label = factory.SubFactory(LabelFactory)
    base_style = random.choices(Release.BaseStyle.values)
    cover_image = factory.django.ImageField(color=factory.Faker("color"))
    format = random.choices(Release.Formats.values)
    sample = factory.Faker("path")
    is_submitted = random.choices([True, False])

    class Meta:
        model = Release