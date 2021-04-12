"""Define tests for Transactions Loader"""
from django.test import TestCase, tag
from transactions.models import Transaction
from ...services.transactions_loader import TransactionsLoader


class TransactionsLoaderTest(TestCase):
    """Test Transactions Loader"""

    @tag('unit')
    def test_loading_transactions(self):
        """test loading transactions"""

        transactions_to_be_loaded = [
            {
                '': '',
                'name': 'Fastly',
                'symbol': 'FSLY.K',
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
                'name': 'Overstockcom',
                'symbol': 'OSTK.O',
                'exchange': 'NASDAQ',
                'open date': '01/05/2021',
                'type': 'BUY',
                'amount': '101.00000000',
                'open price': '53.42',
                'close date': '01/07/2021',
                'close price': '57.16',
                'gain%': '7.00%',
                'net p/l': '$374.00',
            },
        ]

        initial_number_of_transactions = Transaction.objects.count()
        expected_number_of_transactions_loaded = 2
        [saved, duplicates] = TransactionsLoader(transactions_to_be_loaded).load()

        expected_number_of_transactions = initial_number_of_transactions + \
            expected_number_of_transactions_loaded
        self.assertEqual(
            Transaction.objects.count(),
            expected_number_of_transactions
        )

