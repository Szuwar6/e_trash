from django.test import TestCase
from django.urls import reverse
from django.test.client import Client


client = Client()

class AboutViewTests(TestCase):
    def test_sholud_return_200_when_homepage_is_call(self):
        resp = client.get(reverse('homepage'))
        assert resp.status_code == 200
