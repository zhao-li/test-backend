"""Define tests for loading duplicate transactions"""
from django.test import TestCase, tag
from transactions.factories import TransactionFactory
from transactions.models import Transaction
from ....services.transactions_loader import TransactionsLoader


class TestLoadingDuplicates(TestCase):
    """Test Basic Loading Duplicates"""

    def setUp(self):
        self.original_transaction_symbol = 'FSLY.K'
        self.original_transaction = TransactionFactory(
            symbol=self.original_transaction_symbol,
        )

    @tag('unit')
    def test_loading_duplicate_transactions(self):
        """test loading duplicate transactions"""

        transactions_to_be_loaded = [
            {
                '': '',
                'name': 'Fastly',
                'symbol': self.original_transaction_symbol,
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
            {
                '': '',
                'name': 'Fastly',
                'symbol': self.original_transaction_symbol,
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
            self.original_transaction.account,
            transactions_to_be_loaded
        ).load()

        expected_number_of_valid_transactions = 0
        self.assertEqual(
            len(valids),
            expected_number_of_valid_transactions
        )
        expected_number_of_duplicate_transactions = 2
        self.assertEqual(
            len(duplicates),
            expected_number_of_duplicate_transactions
        )
        expected_number_of_dirty_transactions = 0
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

