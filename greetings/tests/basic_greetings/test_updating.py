"""Define tests for updating"""
from django.test import TestCase, tag
from rest_framework import status
from ..helpers.api_service import ApiService
from ..helpers.payload_factory import PayloadFactory
from ...models import Greeting


class UpdatingTests(TestCase):
    """Test updating feature"""

    def setUp(self):
        self.api_service = ApiService()
        original_message = 'Arbitrary Message'
        payload_factory = PayloadFactory({
            'message': original_message,
        })
        response = self.api_service.post(payload_factory.create_payload())
        self.greeting_id = response.json()['data']['id']

    @tag('integration')
    def test_updating(self):
        """test updating works"""

        updated_message = 'Arbitrary Update'
        payload_factory = PayloadFactory({
            'id': self.greeting_id,
            'message': updated_message,
        })
        self.api_service.patch(
            self.greeting_id,
            payload_factory.update_payload(),
        )

        expected_message = updated_message
        self.assertEqual(
            Greeting.objects.get(pk=self.greeting_id).message,
            expected_message
        )

    @tag('integration')
    def test_for_json_api_compliance(self):
        """test response complies with json api spec"""
        payload_factory = PayloadFactory({
            'id': self.greeting_id,
        })
        response = self.api_service.patch(
            self.greeting_id,
            payload_factory.update_payload()
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_key = 'data'
        self.assertTrue(expected_key in response.json())

