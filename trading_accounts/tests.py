"""Define tests for entire module"""
import json
from django.test import Client, TestCase, tag
from rest_framework import status
from .models import TradingAccount

TYPE = 'tradingAccounts'


class TradingAccountsTests(TestCase):
    """Test Trading Account API"""

    def setUp(self):
        self.client = Client()

    @tag('integration')
    def test_fetching(self):
        """test fetchingt"""
        response = self.client.get('/trading-accounts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @tag('integration')
    def test_for_json_api_compliance(self):
        """test response complies with json api spec"""
        response = self.client.get('/trading-accounts/')

        expected_key = 'data'
        self.assertTrue(expected_key in response.json())

    @tag('integration')
    def test_creating(self):
        """test creating"""

        name = 'A Trading Account Name'
        json_data = {
            'data': {
                'type': TYPE,
                'attributes': {
                    'name': name
                }
            }
        }

        response = self.client.post(
            '/trading-accounts/',
            json.dumps(json_data),
            content_type='application/vnd.api+json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expected_name = name
        self.assertEqual(
            TradingAccount.objects.first().name,
            expected_name
        )

    @tag('integration')
    def test_creating_and_getting(self):
        """test creating and getting"""

        name = 'A Trading Account Name'
        json_data = {
            'data': {
                'type': TYPE,
                'attributes': {
                    'name': name
                }
            }
        }

        response = self.client.post(
            '/trading-accounts/',
            json.dumps(json_data),
            content_type='application/vnd.api+json'
        )

        expected_name = name
        self.assertEqual(TradingAccount.objects.first().name, expected_name)

        response = self.client.get('/trading-accounts/')
        first_trading_account_index = 0
        self.assertEqual(
            (response.json()
                ['data'][first_trading_account_index]
                ['attributes']['name']
             ),
            expected_name
        )

