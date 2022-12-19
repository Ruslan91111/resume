import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configuration.settings')

from django.urls import reverse
from rest_framework.test import APITestCase


class MoviesApiTestCase(APITestCase):
    def test_get(self):
        url = reverse('movies-list')
        print(url)
        response = self.client.get(url)
        print(response)


