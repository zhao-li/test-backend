"""Define tests for updating"""
from django.test import TestCase, tag
from rest_framework import status
from ..helpers.api_service import ApiService
from ..helpers.payload_factory import PayloadFactory
from ...factories import TransactionFactory
from ...models import Transaction


class UpdatingTests(TestCase):
    """Test Updating"""

    def setUp(self):
        self.arbitrary_symbol = 'original symbol'
        self.transaction = TransactionFactory(
            symbol=self.arbitrary_symbol,
        )

        self.api_service = ApiService()

    @tag('integration')
    def test_updating(self):
        """test updating"""

        updated_symbol = 'updated symbol'
        payload_factory = PayloadFactory({
            'id': self.transaction.id,
            'symbol': updated_symbol,
        })
        response = self.api_service.patch(
            self.transaction.id,
            payload_factory.update_payload(),
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_symbol = updated_symbol
        self.assertEqual(
            Transaction.objects.get(pk=self.transaction.id).symbol,
            expected_symbol
        )

