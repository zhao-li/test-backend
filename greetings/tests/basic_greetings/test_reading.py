"""Define tests for reading"""
from django.test import TestCase, tag
from rest_framework import status
from ..helpers.api_service import ApiService


class ReadingTests(TestCase):
    """Test reading feature"""

    def setUp(self):
        self.api_service = ApiService()

    @tag('integration')
    def test_reading(self):
        """test reading works"""
        response = self.api_service.get_all()
        expected_number_of_greetings = 0
        self.assertEqual(
            len(response.json()['data']),
            expected_number_of_greetings
        )

    @tag('integration')
    def test_for_json_api_compliance(self):
        """test response complies with json api spec"""
        response = self.api_service.get_all()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_key = 'data'
        self.assertTrue(expected_key in response.json())

