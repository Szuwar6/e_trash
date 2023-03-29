from django.test import TestCase
from django.urls import reverse
from django.test.client import Client

client = Client()


class HomepageViewTests(TestCase):
    def test_sholud_return_200_when_homepage_is_call(self):
        resp = client.get(reverse("homepage"))
        assert resp.status_code == 200


class ClientDetailViewTests(TestCase):
    def test_sholud_return_302_when_clients_detail_view_is_call(self):
        resp = client.get(reverse("base:clients-detail-view"))
        assert resp.status_code == 302


class RecyclerDetailViewTests(TestCase):
    def test_sholud_return_302_when_recycler_detail_view_is_call(self):
        resp = client.get(reverse("base:recycler-detail-view"))
        assert resp.status_code == 302


class OrderDetailViewTests(TestCase):
    def test_sholud_return_302_when_order_user_view_is_call(self):
        resp = client.get(reverse("base:orders-user-view"))
        assert resp.status_code == 302


class HomepageClientViewTests(TestCase):
    def test_sholud_return_200_when_homepage_client_is_call(self):
        resp = client.get(reverse("homepage-client"))
        assert resp.status_code == 200
