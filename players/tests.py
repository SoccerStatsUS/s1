from django.core.urlresolvers import reverse
from django.test import TestCase, Client

class SimpleTest(TestCase):

    def test_urls(self):
        response = self.client.get(reverse("person_index"))
        self.assertEqual(response.status_code, 200)
        url = reverse("person_detail")
        response = self.client.get(url, {"id": 100})
        self.assertEqual(response.status_code, 200)        


