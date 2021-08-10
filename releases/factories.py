import factory
from users.models import User, Label, Profile
from .models import Release
import random
from django.db.models.signals import post_save


# more about using profile and user models in factory boy
# here https://factoryboy.readthedocs.io/en/stable/recipes.html#:~:text=class%20ProfileFactory(factory.django.DjangoModelFactory)%3A
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
    country = "ru"
    album_title = factory.Faker("name")
    release_date = factory.Faker("date_time")
    label = factory.SubFactory(LabelFactory)
    base_style = random.choices(Release.BaseStyle.values)
    cover_image = factory.django.ImageField(color=factory.Faker("color"))
    format = "CD"
    sample = factory.Faker("name")
    is_submitted = random.choices([True, False])[0]

    class Meta:
        model = Release