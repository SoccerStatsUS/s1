from django.core.urlresolvers import reverse
from django.test import TestCase, Client

class SimpleTest(TestCase):

    def test_urls(self):
        response = self.client.get(reverse("stats_index"))
        self.assertEqual(response.status_code, 200)

        url = reverse("year_stats")
        response = self.client.get(url, {"year": 2000})
        self.assertEqual(response.status_code, 200)        
        response = self.client.get(url, {"year": 1990})
        self.assertEqual(response.status_code, 404)        
