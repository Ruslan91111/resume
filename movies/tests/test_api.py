from django.urls import reverse
from rest_framework.test import APITestCase


class MoviesApiTestCase(APITestCase):
    def test_get(self):
        url = reverse('movies_by_category')
        print(url)
        response = self.client.get(url)
        print(response)