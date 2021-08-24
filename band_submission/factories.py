import factory
from users.factories import LabelFactory, UserWithProfileFactory
from .models import BandSubmission
from configuration.settings import BASE_DIR


class BandSubmissionFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")
    email = factory.Faker("email")
    biography = factory.Faker("text")
    demo_sample = f"{BASE_DIR}/releases/test_files/dummy.mp3"
    logo = f"{BASE_DIR}/releases/test_files/dummy.jpg"

    class Meta:
        model = BandSubmission
