import factory
from users.factories import UserFactory, LabelFactory, ProfileFactory
from .models import Release
import random


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

    class Meta:
        model = Release