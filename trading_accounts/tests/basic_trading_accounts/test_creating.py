"""Define tests for creating"""
import json
from django.test import Client, TestCase, tag
from rest_framework import status
from ...models import TradingAccount
from ..constants  import TYPE, PATH, CONTENT_TYPE


class CreatingTests(TestCase):
    """Test Creating"""

    def setUp(self):
        self.client = Client()
        self.name = 'A Trading Account Name'
        self.json_data = {
            'data': {
                'type': TYPE,
                'attributes': {
                    'name': self.name
                }
            }
        }

    @tag('integration')
    def test_for_json_api_compliance(self):
        """test response complies with json api spec"""
        response = self.client.post(
            PATH,
            json.dumps(self.json_data),
            content_type=CONTENT_TYPE,
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expected_key = 'data'
        self.assertTrue(expected_key in response.json())

    @tag('integration')
    def test_creating(self):
        """test creating"""

        initial_number_of_accounts = TradingAccount.objects.count()
        response = self.client.post(
            PATH,
            json.dumps(self.json_data),
            content_type=CONTENT_TYPE,
        )

        expected_number_of_accounts = initial_number_of_accounts + 1
        self.assertEqual(
            TradingAccount.objects.count(),
            expected_number_of_accounts
        )

        account_id = response.json()['data']['id']
        expected_name = self.name
        self.assertEqual(
            TradingAccount.objects.get(pk=account_id).name,
            expected_name
        )

