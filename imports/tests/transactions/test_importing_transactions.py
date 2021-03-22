"""Define tests for importing transactions"""
from django.test import TestCase, tag
from trading_accounts.factories import TradingAccountFactory
from trading_accounts.models import TradingAccount


class ImportingTransactionsTest(TestCase):
    """Test Importing Transactions"""

    def setUp(self):
        payload_factory = TradingAccountFactory()

    @tag('integration')
    def test_importing_transactions_to_account(self):
        """test importing transactions to account"""
        initial_number_of_transactions = TradingAccount.objects.count()

        number_of_transactions_created = 1
        expected_number_of_transactions = (
            initial_number_of_transactions + number_of_transactions_created
        )
        self.assertEqual(
            TradingAccount.objects.count(),
            expected_number_of_transactions
        )

