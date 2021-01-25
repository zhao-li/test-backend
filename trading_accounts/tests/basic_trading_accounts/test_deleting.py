"""Define tests for deleting"""
import json
from django.test import Client, TestCase, tag
from rest_framework import status
from ...models import TradingAccount
from ..constants  import TYPE, PATH, CONTENT_TYPE


class DeletingTests(TestCase):
    """Test Deleting"""

    def setUp(self):
        self.client = Client()
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
            PATH,
            json.dumps(json_data),
            content_type=CONTENT_TYPE,
        )
        self.account_id = response.json()['data']['id']

    @tag('integration')
    def test_for_json_api_compliance(self):
        """test response complies with json api spec"""
        response = self.client.delete(
            PATH + self.account_id + '/',
            content_type = CONTENT_TYPE,
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    @tag('integration')
    def test_deleting(self):
        """test deleting"""

        initial_number_of_accounts = TradingAccount.objects.count()
        response = self.client.delete(
            PATH + self.account_id + '/',
            content_type = CONTENT_TYPE,
        )

        number_of_accounts_deleted = 1
        expected_number_of_accounts = (
            initial_number_of_accounts - number_of_accounts_deleted
        )
        self.assertEqual(
            TradingAccount.objects.count(),
            expected_number_of_accounts
        )
        with self.assertRaises(TradingAccount.DoesNotExist):
            TradingAccount.objects.get(pk=self.account_id)

