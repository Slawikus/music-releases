import factory
from .models import Label
from users.factories import ProfileFactory


class LabelFactory(factory.django.DjangoModelFactory):
    profile = factory.SubFactory(ProfileFactory)
    name = factory.Faker("name")

    class Meta:
        model = Label
