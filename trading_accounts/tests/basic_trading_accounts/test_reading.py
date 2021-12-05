"""Define tests for reading"""
from django.test import TestCase, tag
from rest_framework import status
from ..helpers.api_service import ApiService


class ReadingTests(TestCase):
    """Test Reading"""

    def setUp(self):
        self.api_service = ApiService()

    @tag('integration')
    def test_for_json_api_compliance(self):
        """test response complies with json api spec"""
        response = self.api_service.get_all()

        # pylint:disable=duplicate-code ; is not really recognized by linter
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_key = 'data'
        self.assertTrue(expected_key in response.json())

    @tag('integration')
    def test_reading(self):
        """test reading"""
        response = self.api_service.get_all()
        no_trading_accounts = 0
        self.assertEqual(
            len(response.json()['data']),
            no_trading_accounts
        )

