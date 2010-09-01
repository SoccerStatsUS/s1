from django.core.urlresolvers import reverse
from django.test import TestCase, Client

class SimpleTest(TestCase):

    def test_urls(self):
        response = self.client.get(reverse("teams_index"))
        self.assertEqual(response.status_code, 200)

        # Kansas City Wizards
        url = reverse("team_by_id")
        response = self.client.get(url, {"id": 12})
        self.assertEqual(response.status_code, 200)
        
        url = reverse("team_by_slug")
        response = self.client.get(url, {"slug": 'kansas-city-wizards'})
        self.assertEqual(response.status_code, 200)
        
        url = reverse("team_and_year")
        response = self.client.get(url, {"id": 12, "year": 1996})
        self.assertEqual(response.status_code, 200)        
