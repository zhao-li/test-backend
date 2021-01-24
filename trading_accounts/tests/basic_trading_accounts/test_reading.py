"""Define tests for reading basic"""
from django.test import Client, TestCase, tag
from rest_framework import status
from ..constants  import PATH


class ReadingTests(TestCase):
    """Test Reading"""

    def setUp(self):
        self.client = Client()

    @tag('integration')
    def test_for_json_api_compliance(self):
        """test response complies with json api spec"""
        response = self.client.get(PATH)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_key = 'data'
        self.assertTrue(expected_key in response.json())

    @tag('integration')
    def test_reading(self):
        """test reading"""
        response = self.client.get(PATH)
        no_trading_accounts = 0
        self.assertEqual(
            len(response.json()['data']),
            no_trading_accounts
        )

