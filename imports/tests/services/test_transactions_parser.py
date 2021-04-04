"""Define tests for transaction parser"""
from django.test import TestCase, tag
from ...services.transactions_parser import TransactionsParser


class TransactionsParserTest(TestCase):
    """Test Parsing Transactions"""

    @tag('unit')
    def test_parsing_transactions(self):
        """test parsing transactions"""

        transaction_fieldnames = '''"","Name","Symbol","Exchange","Open Date","Type","Amount","Open Price","Close Date","Close Price","Gain%","Net P/L"'''
        first_transaction = '''"","Fastly","FSLY.K","NYSE","01/07/2021","BUY","100.00000000","86.41","01/08/2021","86.42","0.00%","$0.00"'''
        second_transaction = '''"","Overstockcom","OSTK.O","NASDAQ","01/05/2021","BUY","101.00000000","53.42","01/07/2021","57.16","7.00%","$374.00"'''

        transactions_data = [
            transaction_fieldnames,
            first_transaction,
            second_transaction,
        ]

        transactions = TransactionsParser(transactions_data).parse()

        expected_number_of_transactions = 2
        self.assertEqual(
            len(transactions),
            expected_number_of_transactions
        )

        first_transaction_index = 0
        self.assertEqual(
            transactions[first_transaction_index]["symbol"],
            "FSLY.K"
        )
        self.assertEqual(
            transactions[first_transaction_index]["type"],
            "BUY"
        )
        self.assertEqual(
            transactions[first_transaction_index]["amount"],
            "100.00000000"
        )
        self.assertEqual(
            transactions[first_transaction_index]["open date"],
            "01/07/2021"
        )
        self.assertEqual(
            transactions[first_transaction_index]["open price"],
            "86.41"
        )
        self.assertEqual(
            transactions[first_transaction_index]["close date"],
            "01/08/2021"
        )
        self.assertEqual(
            transactions[first_transaction_index]["close price"],
            "86.42"
        )

        second_transaction_index = 1
        self.assertEqual(
            transactions[second_transaction_index]["symbol"],
            "OSTK.O"
        )
        self.assertEqual(
            transactions[second_transaction_index]["type"],
            "BUY"
        )
        self.assertEqual(
            transactions[second_transaction_index]["amount"],
            "101.00000000"
        )
        self.assertEqual(
            transactions[second_transaction_index]["open date"],
            "01/05/2021"
        )
        self.assertEqual(
            transactions[second_transaction_index]["open price"],
            "53.42"
        )
        self.assertEqual(
            transactions[second_transaction_index]["close date"],
            "01/07/2021"
        )
        self.assertEqual(
            transactions[second_transaction_index]["close price"],
            "57.16"
        )

