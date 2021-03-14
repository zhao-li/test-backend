"""Define tests for reading"""
from django.test import TestCase, tag
from rest_framework import status
from trading_accounts.models import TradingAccount
from users.models import User
from ..helpers.api_service import ApiService
from ..helpers.payload_factory import PayloadFactory
from ...models import Transaction


class ReadingTests(TestCase):
    """Test Reading"""

    def setUp(self):
        self.api_service = ApiService()

        username = 'arbitrary user'
        user = User(username=username)
        user.save()

        account_name = 'arbitrary account name'
        account = TradingAccount(
            name=account_name,
            owner=user,
        )
        account.save()

        self.arbitrary_symbol = 'arbitrary symbol'
        self.transaction = Transaction(
            account_id=account.id,
            symbol=self.arbitrary_symbol,
        )
        self.transaction.save()

    @tag('integration')
    def test_reading_all_transactions(self):
        """test reading all transactions"""

        response = self.api_service.get_all()
        one_transaction = 1
        expected_number_of_transactions = one_transaction
        self.assertEqual(
            len(response.json()['data']),
            expected_number_of_transactions
        )

    @tag('integration')
    def test_reading_specific_transaction(self):
        """test reading specific transaction"""

        response = self.api_service.get_one(self.transaction.id)
        expected_transanction_symbol = self.arbitrary_symbol
        self.assertEqual(
            response.json()['data']['attributes']['symbol'],
            expected_transanction_symbol
        )

