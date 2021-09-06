import factory
from users.factories import ProfileFactory
from .models import BandSubmission
from configuration.settings import BASE_DIR


class BandSubmissionFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")
    album = factory.Faker("name")
    email = factory.Faker("email")
    phone_number = factory.Faker("phone_number")
    biography = factory.Faker("text")
    best_track = f"{BASE_DIR}/releases/test_files/dummy.mp3"
    front_cover = f"{BASE_DIR}/releases/test_files/dummy.jpg"
    profile = factory.SubFactory(ProfileFactory)

    class Meta:
        model = BandSubmission
