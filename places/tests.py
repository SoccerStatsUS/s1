from django.core.urlresolvers import reverse
from django.test import TestCase, Client

class SimpleTest(TestCase):

    def test_urls(self):
        response = self.client.get(reverse("country_index"))
        self.assertEqual(response.status_code, 200)

        url = reverse("country_detail")
        response = self.client.get(url, {"id": 50 })
        self.assertEqual(response.status_code, 200)

        # Look into the context.
        url = reverse("birthplace_detail")
        response = self.client.get(url, {"name": "Dallas"})
        self.assertEqual(response.status_code, 200)
