"""Define tests for loading transactions"""
from django.test import TestCase, tag
from trading_accounts.factories import TradingAccountFactory
from transactions.models import Transaction
from ....services.transactions_loader import TransactionsLoader


class TestBasicLoading(TestCase):
    """Test Basic Loading"""

    def setUp(self):
        self.account = TradingAccountFactory()

    @tag('unit')
    def test_loading_transactions(self):
        """test loading multiple valid transactions"""

        first_transaction_symbol = 'FSLY.K'
        second_transaction_symbol = 'OSTK.O'
        transactions_to_be_loaded = [
            {
                '': '',
                'name': 'Fastly',
                'symbol': first_transaction_symbol,
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
                'symbol': second_transaction_symbol,
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
        [saved, duplicates, failed] = TransactionsLoader(
            self.account,
            transactions_to_be_loaded
        ).load()

        expected_number_of_transactions = initial_number_of_transactions + \
            expected_number_of_transactions_loaded
        self.assertEqual(
            Transaction.objects.count(),
            expected_number_of_transactions
        )

        transactions_in_database = Transaction.objects.all()
        first_transaction_index = 0
        self.assertEqual(
            transactions_in_database[first_transaction_index].symbol,
            first_transaction_symbol
        )
        second_transaction_index = 1
        self.assertEqual(
            transactions_in_database[second_transaction_index].symbol,
            second_transaction_symbol
        )


