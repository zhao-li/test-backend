"""Define tests for entire lifecycle"""
import json
from django.test import Client, TestCase, tag
from rest_framework import status
from ..constants import TYPE, PATH, CONTENT_TYPE


class LIfeCycleTests(TestCase):
    """Test Life Cycle"""

    def setUp(self):
        self.client = Client()

    @tag('integration')
    def test_life_cycle(self):
        """test life cycle"""

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
        returned_json = response.json()
        account_id = returned_json['data']['id']

        response = self.client.get(PATH + account_id + '/')
        expected_name = original_name
        self.assertEqual(
            response.json()['data']['attributes']['name'],
            expected_name
        )

        updated_json_data = returned_json
        updated_name = 'An Updated Trading Account Name'
        updated_json_data['data']['attributes']['name'] = updated_name
        response = self.client.patch(
            PATH + account_id + '/',
            data=json.dumps(updated_json_data),
            content_type=CONTENT_TYPE,
        )

        response = self.client.get(PATH + account_id + '/')
        expected_name = updated_name
        self.assertEqual(
            response.json()['data']['attributes']['name'],
            expected_name
        )

        response = self.client.delete(
            PATH + account_id + '/',
            content_type=CONTENT_TYPE,
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

