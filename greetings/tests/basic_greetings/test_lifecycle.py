"""Define tests for life cycle"""
from django.test import TestCase, tag
from rest_framework import status
from ..helpers.api_service import ApiService
from ..helpers.payload_factory import PayloadFactory


class LifeCycleTests(TestCase):
    """Test life cycle"""

    def setUp(self):
        self.api_service = ApiService()

    @tag('integration')
    def test_life_cycle(self):
        """test life cycle works"""

        original_message = 'Arbitrary Message'
        payload_factory = PayloadFactory({
            'message': original_message,
        })
        response = self.api_service.post(payload_factory.create_payload())
        greeting_id = response.json()['data']['id']

        response = self.api_service.get_one(greeting_id)
        expected_message = original_message
        self.assertEqual(
            response.json()['data']['attributes']['message'],
            expected_message
        )

        updated_payload = response.json()
        updated_message = 'Arbitrary Update'
        updated_payload['data']['attributes']['message'] = updated_message
        response = self.api_service.patch(greeting_id, updated_payload)

        response = self.api_service.get_one(greeting_id)
        expected_message = updated_message
        self.assertEqual(
            response.json()['data']['attributes']['message'],
            expected_message
        )

        response = self.api_service.delete(greeting_id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.api_service.get_one(greeting_id)
        index_of_first_error = 0
        expected_code = 'not_found'
        self.assertEqual(
            response.json()['errors'][index_of_first_error]['code'],
            expected_code
        )

