"""Define tests for entire lifecycle"""
from django.test import TestCase, tag
from rest_framework import status
from users.models import User
from ..helpers.api_service import ApiService
from ..helpers.payload_factory import PayloadFactory


class LIfeCycleTests(TestCase):
    """Test Life Cycle"""

    def setUp(self):
        self.api_service = ApiService()
        username = 'arbitrary user'
        self.user = User(username=username)
        self.user.save()
        
    @tag('integration')
    def test_life_cycle(self):
        """test life cycle"""

        original_name = 'A Trading Account Name'
        payload_factory = PayloadFactory({
            'name': original_name,
            'owner_id': self.user.id,
        })
        response = self.api_service.post(payload_factory.create_payload())
        account_id = response.json()['data']['id']

        response = self.api_service.get_one(account_id)
        expected_name = original_name
        self.assertEqual(
            response.json()['data']['attributes']['name'],
            expected_name
        )

        updated_payload = response.json()
        updated_name = 'An Updated Trading Account Name'
        updated_payload['data']['attributes']['name'] = updated_name
        response = self.api_service.patch(account_id, updated_payload)

        response = self.api_service.get_one(account_id)
        expected_name = updated_name
        self.assertEqual(
            response.json()['data']['attributes']['name'],
            expected_name
        )

        response = self.api_service.delete(account_id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

