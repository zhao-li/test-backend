"""Define tests for reading"""
from django.test import TestCase, tag
from rest_framework import status
from trading_accounts.models import TradingAccount
from users.models import User
from ..helpers.api_service import ApiService
from ..helpers.payload_factory import PayloadFactory


class ReadingTests(TestCase):
    """Test Reading"""

    def setUp(self):
        self.api_service = ApiService()

    @tag('integration')
    def test_reading_no_transactions(self):
        """test reading no transactions"""
        response = self.api_service.get_all()
        no_transactions = 0

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_key = 'data'
        self.assertTrue(expected_key in response.json())

        self.assertEqual(
            len(response.json()['data']),
            no_transactions
        )

    @tag('integration')
    def test_reading_one_transactions(self):
        """test reading one transactions"""
        username = 'arbitrary user'
        user = User(username=username)
        user.save()

        account_name = 'arbitrary account name'
        account = TradingAccount(
            name=account_name,
            owner=user,
        )
        account.save()

        arbitrary_symbol = 'arbitrary symbol'
        payload_factory = PayloadFactory({
            'account_id': account.id,
            'symbol': arbitrary_symbol,
        })

        response = self.api_service.post(
            payload_factory.create_payload()
        )
        transaction_id = response.json()['data']['id']

        response = self.api_service.get_all()
        one_transaction = 1
        expected_number_of_transactions = one_transaction
        self.assertEqual(
            len(response.json()['data']),
            expected_number_of_transactions
        )

        first_returned_transaction = 0
        expected_transanction_symbol = arbitrary_symbol
        self.assertEqual(
            response.json()['data'][first_returned_transaction]['attributes']['symbol'],
            expected_transanction_symbol
        )

