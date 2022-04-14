"""Define tests for batch upload"""
import os
from django.test import tag, TestCase
from rest_framework import status
from trading_accounts.factories import TradingAccountFactory
from ..helpers.api_service import ApiService
from ..helpers.payload_factory import PayloadFactory
from ...models import Transaction


class BatchUploadingTests(TestCase):
    """Test Batch Uploading"""

    def setUp(self):
        self.account = TradingAccountFactory()
        self.api_service = ApiService()

    @tag('integration')
    def test_batch_uploading_valid_file(self):
        """test batch uploading valid file"""

        initial_number_of_transactions = Transaction.objects.count()
        payload_factory = PayloadFactory(overrides={
            'account_id': self.account.id,
        })

        current_path = os.path.dirname(__file__)
        with open(os.path.join(current_path, 'basic.csv')) as file:
            response = self.api_service.batch_upload(
                payload_factory.file_upload_payload(file)
            )

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

        number_of_transactions_in_file = 2
        expected_number_of_transactions = (
            initial_number_of_transactions + number_of_transactions_in_file
        )
        final_number_of_transactions = Transaction.objects.count()
        self.assertEqual(
            final_number_of_transactions,
            expected_number_of_transactions
        )

        transactions_in_database = Transaction.objects.all()

        first_transaction_index = 0
        expected_symbol_of_first_transaction = 'FSLY.K'
        self.assertEqual(
            transactions_in_database[first_transaction_index].symbol,
            expected_symbol_of_first_transaction
        )
        self.assertEqual(
            transactions_in_database[first_transaction_index].account,
            self.account
        )

        second_transaction_index = 1
        expected_symbol_of_second_transaction = 'OSTK.O'
        self.assertEqual(
            transactions_in_database[second_transaction_index].symbol,
            expected_symbol_of_second_transaction
        )
        self.assertEqual(
            transactions_in_database[second_transaction_index].account,
            self.account
        )

    @tag('integration')
    def test_batch_uploading_invalid_file(self):
        """test uploading invalid file"""

        initial_number_of_transactions = Transaction.objects.count()
        payload_factory = PayloadFactory(overrides={
            'account_id': self.account.id,
        })

        current_path = os.path.dirname(__file__)
        read_mode = 'r'
        byte_format = 'b'
        with open(
                os.path.join(current_path, 'bad_file.jpg'),
                read_mode + byte_format
        ) as file:
            response = self.api_service.batch_upload(
                payload_factory.file_upload_payload(file)
            )

        self.assertEqual(
            response.status_code,
            status.HTTP_422_UNPROCESSABLE_ENTITY
        )

        number_of_transactions_in_file = 0
        expected_number_of_transactions = (
            initial_number_of_transactions + number_of_transactions_in_file
        )
        final_number_of_transactions = Transaction.objects.count()
        self.assertEqual(
            final_number_of_transactions,
            expected_number_of_transactions
        )

