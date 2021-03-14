"""Define tests for reading"""
from django.test import TestCase, tag
from ..helpers.api_service import ApiService
from ...factories import TransactionFactory


class ReadingTests(TestCase):
    """Test Reading"""

    def setUp(self):
        self.arbitrary_symbol = 'arbitrary symbol'
        self.transaction = TransactionFactory(
            symbol=self.arbitrary_symbol,
        )

        self.api_service = ApiService()

    @tag('integration')
    def test_reading_all_transactions(self):
        """test reading all transactions"""

        response = self.api_service.get_all()
        one_transaction = 1
        expected_number_of_transactions = one_transaction
        self.assertEqual(
            len(response.json()['data']),
            expected_number_of_transactions
        )

    @tag('integration')
    def test_reading_specific_transaction(self):
        """test reading specific transaction"""

        response = self.api_service.get_one(self.transaction.id)
        expected_transanction_symbol = self.arbitrary_symbol
        self.assertEqual(
            response.json()['data']['attributes']['symbol'],
            expected_transanction_symbol
        )

