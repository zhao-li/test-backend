"""Define tests for transaction parser"""
from django.test import TestCase, tag
from ...services.transaction_parser import TransactionParser


class TransactionParserTest(TestCase):
    """Test Parsing Transactions"""

    @tag('unit')
    def test_parsing_transaction(self):
        """test parsing transactions"""

        with open(
            'imports/tests/services/transactions.csv'
        ) as file_pointer:
            raw_data_string = file_pointer.read()
            parser = TransactionParser(raw_data_string)

