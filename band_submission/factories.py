import factory
from users.factories import LabelFactory, UserWithProfileFactory
from .models import BandSubmissionLink, BandSubmission
from configuration.settings import BASE_DIR


class BandSubmissionLinkFactory(factory.django.DjangoModelFactory):
    profile = factory.SubFactory(UserWithProfileFactory)
    label = factory.SubFactory(LabelFactory)
    slug = factory.Faker("password")

    class Meta:
        model = BandSubmissionLink


class BandSubmissionFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")
    email = factory.Faker("email")
    biography = factory.Faker("text")
    demo_sample = f"{BASE_DIR}/releases/test_files/dummy.mp3"
    logo = f"{BASE_DIR}/releases/test_files/dummy.jpg"

    class Meta:
        model = BandSubmission
