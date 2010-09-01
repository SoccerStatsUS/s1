from django.core.urlresolvers import reverse
from django.test import TestCase, Client

class SimpleTest(TestCase):

    def test_urls(self):
        response = self.client.get(reverse("salaries_index"))
        self.assertEqual(response.status_code, 200)

        url = reverse("salaries_by_year")
        response = self.client.get(url, {"year": 2009})
        self.assertEqual(response.status_code, 200)        
        response = self.client.get(url, {"year": 2005})
        self.assertEqual(response.status_code, 404)

        # Test for teams
        pass
