"""Define tests for loading transaction without symbol"""
from django.test import TestCase, tag
from trading_accounts.factories import TradingAccountFactory
from transactions.models import Transaction
from ....services.loader import Loader


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
                'open date': '01/05/2021',
                'type': 'BUY',
                'amount': '100.00000000',
                'open price': '86.41',
                'close date': '01/10/2021',
                'close price': '86.42',
                'gain%': '0.00%',
                'net p/l': '$0.00'
            },
        ]

        initial_number_of_transactions = Transaction.objects.count()
        [valids, duplicates, dirties] = Loader(
            self.account,
            transaction_to_be_loaded
        ).load()

        expected_number_of_valid_transactions = 0
        self.assertEqual(
            len(valids),
            expected_number_of_valid_transactions
        )
        # pylint: disable=all; keeping tests DAMP requires some duplicate code
        # unable to just disable duplicate-code:
        # https://github.com/PyCQA/pylint/issues/214#issuecomment-506642328
        expected_number_of_duplicate_transactions = 0
        self.assertEqual(
            len(duplicates),
            expected_number_of_duplicate_transactions
        )
        # pylint: enable=all
        expected_number_of_dirty_transactions = 1
        self.assertEqual(
            len(dirties),
            expected_number_of_dirty_transactions
        )

        # pylint: disable=all; keeping tests DAMP requires some duplicate code
        # unable to just disable duplicate-code:
        # https://github.com/PyCQA/pylint/issues/214#issuecomment-506642328
        expected_number_of_transactions = initial_number_of_transactions + \
            expected_number_of_valid_transactions
        self.assertEqual(
            Transaction.objects.count(),
            expected_number_of_transactions
        )
        # pylint: enable=all

