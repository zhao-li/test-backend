"""Define tests for importing transactions"""
from django.test import TestCase, tag
from rest_framework import status
from trading_accounts.factories import TradingAccountFactory
from trading_accounts.models import TradingAccount
from transactions.models import Transaction
from ..helpers.api_service import ApiService


class ImportingTransactionsTest(TestCase):
    """Test Importing Transactions"""

    def setUp(self):
        self.account = TradingAccountFactory()
        self.api_service = ApiService()

    @tag('integration')
    def test_importing_transactions_to_account(self):
        """test importing transactions to account"""
        initial_number_of_transactions = TradingAccount.objects.count()

        with open(
            'imports/tests/transactions/transactions.csv'
        ) as file_pointer:
            response = self.api_service.post_transactions(
                self.account.id,
                file_pointer
            )

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

        number_of_transactions_created = 1
        expected_number_of_transactions = (
            initial_number_of_transactions + number_of_transactions_created
        )
        self.assertEqual(
            TradingAccount.objects.count(),
            expected_number_of_transactions
        )

        transactions_in_database = Transaction.objects.get()
        first_transaction_index = 0
        expected_symbol_of_first_transaction = 'AAPL'
        self.assertEqual(
            transactions_in_database[first_transaction_index].symbol(),
            expected_symbol_of_first_transaction
        )
        self.assertEqual(
            transactions_in_database[first_transaction_index].account().id,
            self.account.id
        )

