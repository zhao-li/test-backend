"""Define tests for transaction parser"""
from django.test import TestCase, tag
from ...services.transactions_parser import TransactionsParser


class TransactionsParserTest(TestCase):
    """Test Parsing Transactions"""

    @tag('unit')
    def test_parsing_transactions(self):
        """test parsing transactions"""

        transaction_fieldnames = '''"","Name","Symbol","Exchange","Open Date","Type","Amount","Open Price","Current Price","Extended Hours","Extended Hours (%)","Prev.","Market Value","Commission","Net P/L%","Weight","Daily P/L","Daily P/L%","Net P/L","Next Earnings Date"'''
        first_transaction = '''"","Unity Software","U","NYSE","01/08/2021","BUY","35.00000000","147.22","146.20","146.43","0.16%","138.57","$5,117.00","$0.00","-0.69%","3.09%","$267.05","5.51%","-$35.70","May 13, 2021"'''
        second_transaction = '''"","Fastly","FSLY.K","NYSE","01/07/2021","BUY","100.00000000","86.41","88.22","88.25","0.03%","86.91","$8,822.00","$0.00","2.09%","5.33%","$131.00","1.51%","$181.00","May 12, 2021"'''
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
            "U"
        )

        second_transaction_index = 1
        self.assertEqual(
            transactions[second_transaction_index]["symbol"],
            "FSLY.K"
        )

