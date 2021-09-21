from django.db.utils import IntegrityError
from django.test import TestCase

from users.factories import LabelFactory, ProfileFactory, UserWithProfileFactory


class LabelTest(TestCase):
    def setUp(self):
        self.profile = ProfileFactory()
        self.name = 'Roadrunner Records'
        self.description = 'Roadrunner Records drives the collision of culture and heavy music. '\
                           ' Founded in 1980, the company launched in Europe as an independent '\
                           'importer of American metal albums. Planting roots in New York City '\
                           'during 1986, it emerged as the preeminent label for homegrown heavy '\
                           'metal. Throughout the eighties and nineties, the independent label '\
                           'ignited the careers of influential alumni, including King Diamond, Machine '\
                           'Head, Sepultura, and Type O Negative. Achieving number one albums, '\
                           'GRAMMY® Awards, and multiplatinum success, Roadrunner Records carries '\
                           'on a tradition of mainstream infiltration with a current class comprised '\
                           'of Code Orange, Coheed and Cambria, Corey Taylor, Dana Dentata, FEVER 333, '\
                           'Gojira, Slipknot, THEORY, Trivium, and Turnstile. As a subsidiary of '\
                           'Elektra Music Group since 2018, Roadrunner Records continues four decades '\
                           'of excellence in heavy metal, hard rock, and rock, remaining a lifestyle '\
                           'as much as it is a label.'

        self.label = LabelFactory(profile=self.profile, name=self.name, description=self.description)

    # Fields

    def test_it_has_profile(self):
        self.assertEqual(self.profile, self.label.profile)

    def test_it_has_name(self):
        self.assertEqual(self.name, self.label.name)

    def test_it_has_description(self):
        self.assertEqual(self.description, self.label.description)

    def test_it_has_logo(self):
        pass  # TODO: add test later

    def test_it_has_is_main(self):
        self.assertFalse(self.label.is_main)

    # Relations

    def test_it_defines_backward_relation_on_profile(self):
        self.assertEqual(self.label, self.profile.labels.get())

    # Meta

    def test_one_profile_cannot_have_two_labels_with_the_same_name(self):
        with self.assertRaises(IntegrityError) as error:
            LabelFactory(profile=self.profile, name=self.name)

        self.assertIn('unique_label_per_profile', error.exception.args[0])

    def test_one_profile_cannot_have_two_main_labels(self):
        self.label.is_main = True
        self.label.save()

        with self.assertRaises(IntegrityError) as error:
            LabelFactory.create(profile=self.profile, is_main=True)

        self.assertIn('unique_main_label_per_profile', error.exception.args[0])

    # Methods

    def test_string_representation(self):
        self.assertEqual(self.name, str(self.label))

    def test_belongs_to_user(self):
        self.assertTrue(self.label.belongs_to_user(self.profile.user))

        another_user = UserWithProfileFactory.create()

        self.assertFalse(self.label.belongs_to_user(another_user))
