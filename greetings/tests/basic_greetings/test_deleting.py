"""Define tests for deleting"""
from django.test import TestCase, tag
from rest_framework import status
from ..helpers.api_service import ApiService
from ...models import Greeting


class DeletingTests(TestCase):
    """Test deleting feature"""

    def setUp(self):
        self.api_service = ApiService()
        greeting = Greeting(
            message='Arbitrary Message',
        )
        greeting.save()
        self.greeting_id = greeting.id

    @tag('integration')
    def test_deleting(self):
        """test deleting"""

        initial_number_of_greetings = Greeting.objects.count()
        self.api_service.delete(self.greeting_id)

        expected_number_of_greetings_deleted = 1
        expected_number_of_greetings_remaining = (
            initial_number_of_greetings - expected_number_of_greetings_deleted
        )
        self.assertEqual(
            Greeting.objects.count(),
            expected_number_of_greetings_remaining
        )
        with self.assertRaises(Greeting.DoesNotExist):
            Greeting.objects.get(pk=self.greeting_id)

    @tag('integration')
    def test_for_json_api_compliance(self):
        """test response complies with json api spec"""
        response = self.api_service.delete(self.greeting_id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

