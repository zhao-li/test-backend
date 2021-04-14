"""Define tests for loading transaction without symbol"""
from django.test import TestCase, tag
from trading_accounts.factories import TradingAccountFactory
from transactions.models import Transaction
from ....services.transactions_loader import TransactionsLoader


class TestLoadingTransactionWithoutSymbol(TestCase):
    """Test Loading Transaction Without Symbol"""

    def setUp(self):
        self.account = TradingAccountFactory()

    @tag('unit')
    def test_loading_transaction_without_symbol(self):
        """test loading transaction without symbol"""

        transaction_to_be_loaded = [
            {
                '': '',
                'name': 'Fastly',
                'exchange': 'NYSE',
                'open date': '01/07/2021',
                'type': 'BUY',
                'amount': '100.00000000',
                'open price': '86.41',
                'close date': '01/08/2021',
                'close price': '86.42',
                'gain%': '0.00%',
                'net p/l': '$0.00'
            },
        ]

        initial_number_of_transactions = Transaction.objects.count()
        [valids, duplicates, dirties] = TransactionsLoader(
            self.account,
            transaction_to_be_loaded
        ).load()

        expected_number_of_valid_transactions = 0
        self.assertEqual(
            len(valids),
            expected_number_of_valid_transactions
        )
        expected_number_of_duplicate_transactions = 0
        self.assertEqual(
            len(duplicates),
            expected_number_of_duplicate_transactions
        )
        expected_number_of_dirty_transactions = 1
        self.assertEqual(
            len(dirties),
            expected_number_of_dirty_transactions
        )

        expected_number_of_transactions = initial_number_of_transactions + \
            expected_number_of_valid_transactions
        self.assertEqual(
            Transaction.objects.count(),
            expected_number_of_transactions
        )

