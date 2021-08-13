import factory
from users.factories import UserFactory, LabelFactory, ProfileFactory
from datetime import datetime
from .models import Release
import random
from factory.fuzzy import FuzzyDateTime
import pytz

class ReleaseFactory(factory.django.DjangoModelFactory):
    profile = factory.SubFactory(ProfileFactory)
    band_name = factory.Faker("name")
    country = "ru"
    album_title = factory.Faker("name")
    submitted_at = FuzzyDateTime(
        datetime(2010, 1, 1, 1, 1, 1, 1, pytz.utc),
        datetime(2034, 1, 1, 1, 1, 1, 1, pytz.utc)
    )
    release_date = factory.Faker("date_time")
    label = factory.SubFactory(LabelFactory)
    base_style = random.choices(Release.BaseStyle.values)
    cover_image = factory.django.ImageField(color=factory.Faker("color"))
    format = "CD"
    sample = factory.Faker("name")

    class Meta:
        model = Release