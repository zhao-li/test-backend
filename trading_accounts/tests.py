"""Definte tests for entire module"""
from django.test import Client, TestCase, tag
from rest_framework import status


class TradingAccountTests(TestCase):
    """Test Trading Account API"""

    def setUp(self):
        self.client = Client()

    @tag('integration')
    def test_fetching_list(self):
        """test getting a list of trading accounts"""
        response = self.client.get('/trading-accounts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

