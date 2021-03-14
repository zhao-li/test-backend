"""Define tests for creating"""
from django.test import TestCase, tag
from rest_framework import status
from trading_accounts.factories import TradingAccountFactory
from ..helpers.api_service import ApiService
from ..helpers.payload_factory import PayloadFactory
from ...models import Transaction


class CreatingTests(TestCase):
    """Test Creating"""

    def setUp(self):
        self.arbitrary_account_name = 'arbitrary account name'
        self.account = TradingAccountFactory(
            name=self.arbitrary_account_name,
        )

        self.api_service = ApiService()

    @tag('integration')
    def test_creating_with_trading_account(self):
        """test creating with associated trading account"""

        initial_number_of_transactions = Transaction.objects.count()

        arbitrary_symbol = 'arbitrary symbol'
        payload_factory = PayloadFactory({
            'account_id': self.account.id,
            'symbol': arbitrary_symbol,
        })

        response = self.api_service.post(
            payload_factory.create_payload()
        )
        transaction_id = response.json()['data']['id']

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        number_of_transactions_created = 1
        expected_number_of_transactions = (
            initial_number_of_transactions + number_of_transactions_created
        )
        self.assertEqual(
            Transaction.objects.count(),
            expected_number_of_transactions
        )

        transaction_in_database = Transaction.objects.get(pk=transaction_id)
        expected_symbol = arbitrary_symbol
        self.assertEqual(
            transaction_in_database.symbol,
            expected_symbol
        )

        expected_account_name = self.arbitrary_account_name
        self.assertEqual(
            transaction_in_database.account.name,
            expected_account_name
        )

