"""Define tests for creating"""
from django.test import TestCase, tag
from rest_framework import status
from ..helpers.api_service import ApiService
from ..helpers.payload_factory import PayloadFactory
from ...models import Greeting


class CreatingTests(TestCase):
    """Test kreating functionality"""

    def setUp(self):
        self.api_service = ApiService()
        self.message = 'An Arbitrary Message'
        self.payload_factory = PayloadFactory({
            'message': self.message,
        })

    @tag('integration')
    def test_creating(self):
        """test creating worked"""

        initial_number_of_greetings = Greeting.objects.count()
        response = self.api_service.post(self.payload_factory.create_payload())

        expected_number_of_greetings_created = 1
        expected_number_of_total_greetings = (
            initial_number_of_greetings + expected_number_of_greetings_created
        )
        self.assertEqual(
            Greeting.objects.count(),
            expected_number_of_total_greetings
        )

        greeting_id = response.json()['data']['id']
        expected_message = self.message
        self.assertEqual(
            Greeting.objects.get(pk=greeting_id).message,
            expected_message
        )

    @tag('integration')
    def test_for_json_api_compliance(self):
        """test response complies with json api spec"""
        response = self.api_service.post(self.payload_factory.create_payload())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expected_key = 'data'
        self.assertTrue(expected_key in response.json())

