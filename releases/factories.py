import random
from datetime import datetime
import factory
import pytz
from factory.fuzzy import FuzzyDateTime
from users.factories import LabelFactory, ProfileFactory
from .models import Release, MarketingInfos
from configuration.settings import BASE_DIR


class ReleaseFactory(factory.django.DjangoModelFactory):
    profile = factory.SubFactory(ProfileFactory)
    band_name = factory.Faker("name")
    country = "ru"
    album_title = factory.Faker("name")
    submitted_at = FuzzyDateTime(
        datetime(2010, 1, 1, 1, 1, 1, 1, pytz.utc),
        datetime(2034, 1, 1, 1, 1, 1, 1, pytz.utc)
    )
    release_date = factory.Faker("date")
    label = factory.SubFactory(
        LabelFactory, profile=factory.SelfAttribute('..profile')
    )
    base_style = random.choices(Release.BaseStyle.values)
    cover_image = factory.django.ImageField(color=factory.Faker("color"))
    format = "CD"
    sample = f"{BASE_DIR}/releases/test_files/dummy.mp3"

    class Meta:
        model = Release


class MarketingInfosFactory(factory.django.DjangoModelFactory):
    release = factory.SubFactory(ReleaseFactory)
    style = factory.Faker("name")
    release_overview = factory.Faker("text")
    youtube_url = factory.Faker("url")
    soundcloud_url = factory.Faker("url")
    press_feedback = factory.Faker("text")

    class Meta:
        model = MarketingInfos
