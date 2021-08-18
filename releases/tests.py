from django.test import TestCase, Client
from django.urls import reverse_lazy

# Create your tests here.
class TestViews(TestCase):

    def test_excel(self):
        client = Client()
        response = client.get(reverse_lazy("get_example_excel"))
        self.assertEqual(response.status_code, 200)