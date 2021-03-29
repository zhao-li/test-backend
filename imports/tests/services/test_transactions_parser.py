"""Define tests for transaction parser"""
from django.test import TestCase, tag
from ...services.transactions_parser import TransactionsParser


class TransactionsParserTest(TestCase):
    """Test Parsing Transactions"""

    @tag('unit')
    def test_parsing_transactions(self):
        """test parsing transactions"""

        with open(
            'imports/tests/services/transactions.csv'
        ) as file_pointer:
            raw_data_string = file_pointer.read()
            transactions = TransactionsParser(raw_data_string).parse()

