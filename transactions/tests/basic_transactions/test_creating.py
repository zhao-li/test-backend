"""Define tests for creating"""
from django.test import TestCase, tag
from rest_framework import status
from trading_accounts.models import TradingAccount
from users.models import User
from ..helpers.api_service import ApiService
from ..helpers.payload_factory import PayloadFactory
from ...models import Transaction


class CreatingTests(TestCase):
    """Test Creating"""

    def setUp(self):
        self.api_service = ApiService()
        pass

    @tag('integration')
    def test_creating_with_trading_account(self):
        """test creating with associated trading account"""

        initial_number_of_transactions = Transaction.objects.count()

        username = 'arbitrary user'
        user = User(username=username)
        user.save()

        account_name = 'arbitrary account name'
        account = TradingAccount(
            name = account_name,
            owner = user,
        )
        account.save()

        payload_factory = PayloadFactory({
            'account_id': account.id,
        })

        response = self.api_service.post(
            payload_factory.create_payload()
        )
        transaction_id = response.json()['data']['id']

        number_of_transactions_created = 1
        expected_number_of_transactions = (
            initial_number_of_transactions + number_of_transactions_created
        )
        self.assertEqual(
            Transaction.objects.count(),
            expected_number_of_transactions
        )

        transaction_in_database = Transaction.objects.get(pk=transaction_id)
        self.assertEqual(
            transaction_in_database.id,
            int(transaction_id) # TODO replace with some important transaction attribute
        )
        self.assertEqual(
            transaction_in_database.account.name,
            account_name
        )
        self.assertEqual(
            transaction_in_database.account.owner.username,
            username
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expected_key = 'data'
        self.assertTrue(expected_key in response.json())

