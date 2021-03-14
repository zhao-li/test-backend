"""Define tests for deleting"""
from django.test import TestCase, tag
from rest_framework import status
from ..helpers.api_service import ApiService
from ...factories import TransactionFactory
from ...models import Transaction


class DeletingTests(TestCase):
    """Test Deleting"""

    def setUp(self):
        self.arbitrary_symbol = 'original symbol'
        self.transaction = TransactionFactory(
            symbol=self.arbitrary_symbol,
        )

        self.api_service = ApiService()

    @tag('integration')
    def test_deleting(self):
        """test deleting"""

        initial_number_of_transactions = Transaction.objects.count()
        response = self.api_service.delete(self.transaction.id)

        number_of_transactions_deleted = 1
        expected_number_of_transactions = (
            initial_number_of_transactions - number_of_transactions_deleted
        )
        self.assertEqual(
            Transaction.objects.count(),
            expected_number_of_transactions
        )
        with self.assertRaises(Transaction.DoesNotExist):
            Transaction.objects.get(pk=self.transaction.id)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

