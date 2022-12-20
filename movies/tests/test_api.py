import os

from rest_framework.reverse import reverse

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configuration.settings')
import django
django.setup()
from django.urls import reverse

from rest_framework.test import APITestCase


class MoviesApiTestCase(APITestCase):
    def test_get(self):
        url = reverse('movie-list')
        print(url)
        response = self.client.get(url)
        print(response)


