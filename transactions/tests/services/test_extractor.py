"""Define tests for Transactions Extractor"""
import os
from django.test import tag, TestCase
from ...services.extractor import Extractor


class ExtractorTest(TestCase):
    """Test Transactions Extractor"""

    @tag('unit')
    def test_extracting_transactions(self):
        """test extracting transactions"""

        current_path = os.path.dirname(__file__)
        with open(os.path.join(current_path, 'portfolio.csv')) as file_pointer:
            raw_data_string = file_pointer.read()
            transactions = Extractor(raw_data_string).extract()

        expected_number_of_headings = 1
        expected_number_of_transactions = 2
        expected_number_of_rows = expected_number_of_headings + \
            expected_number_of_transactions
        self.assertEqual(
            len(transactions),
            expected_number_of_rows
        )

        first_transaction_index = 1
        self.assertEqual(
            transactions[first_transaction_index],
            '''"","Fastly","FSLY.K","NYSE","01/07/2021","BUY","100.00000000","86.41","01/08/2021","86.41","0.00%","$0.00"'''  # nopep8 pylint: disable=line-too-long
        )

        second_transaction_index = 2
        self.assertEqual(
            transactions[second_transaction_index],
            '''"","Overstockcom","OSTK.O","NASDAQ","01/05/2021","BUY","100.00000000","53.42","01/07/2021","57.16","7.00%","$374.00"'''  # nopep8 pylint: disable=line-too-long
        )

