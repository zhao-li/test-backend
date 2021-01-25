"""Define tests for creating"""
from django.test import TestCase, tag
from rest_framework import status
from ..helpers.api_service import ApiService
from ..helpers.payload_factory import PayloadFactory
from ...models import TradingAccount


class CreatingTests(TestCase):
    """Test Creating"""

    def setUp(self):
        self.api_service = ApiService()
        self.name = 'A Trading Account Name'
        self.payload_factory = PayloadFactory({
            'name': self.name,
        })

    @tag('integration')
    def test_for_json_api_compliance(self):
        """test response complies with json api spec"""
        response = self.api_service.post(self.payload_factory.create_payload())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expected_key = 'data'
        self.assertTrue(expected_key in response.json())

    @tag('integration')
    def test_creating(self):
        """test creating"""

        initial_number_of_accounts = TradingAccount.objects.count()
        response = self.api_service.post(self.payload_factory.create_payload())

        number_of_accounts_created = 1
        expected_number_of_accounts = (
            initial_number_of_accounts + number_of_accounts_created
        )
        self.assertEqual(
            TradingAccount.objects.count(),
            expected_number_of_accounts
        )

        account_id = response.json()['data']['id']
        expected_name = self.name
        self.assertEqual(
            TradingAccount.objects.get(pk=account_id).name,
            expected_name
        )

