"""Define tests for updating"""
import json
from django.test import Client, TestCase, tag
from rest_framework import status
from ...models import TradingAccount
from ..constants import TYPE, PATH, CONTENT_TYPE


class UpdatingTests(TestCase):
    """Test Updating"""

    def setUp(self):
        self.client = Client()
        original_name = 'A Trading Account Name'
        json_data = {
            'data': {
                'type': TYPE,
                'attributes': {
                    'name': original_name
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
        json_data = {
            'data': {
                'type': TYPE,
                'id': self.account_id,
                'attributes': {
                    'name': 'arbitrary name'
                }
            }
        }

        response = self.client.patch(
            PATH + self.account_id + '/',
            data=json.dumps(json_data),
            content_type=CONTENT_TYPE,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_key = 'data'
        self.assertTrue(expected_key in response.json())

    @tag('integration')
    def test_updating(self):
        """test updating"""

        updated_name = 'An Updated Trading Account Name'
        json_data = {
            'data': {
                'type': TYPE,
                'id': self.account_id,
                'attributes': {
                    'name': updated_name
                }
            }
        }

        self.client.patch(
            PATH + self.account_id + '/',
            data=json.dumps(json_data),
            content_type=CONTENT_TYPE,
        )

        expected_name = updated_name
        self.assertEqual(
            TradingAccount.objects.get(pk=self.account_id).name,
            expected_name
        )

