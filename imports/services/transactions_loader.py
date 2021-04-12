"""Define Loader for Transactions"""
from django.core.exceptions import ValidationError
from django.db.transaction import TransactionManagementError
from django.db.utils import IntegrityError
from transactions.models import Transaction


class TransactionsLoader():
    """
    A loader for transactions
    Note: load means saving to storage
    Input: 
    Example: 
    Output: A list of 3 lists
      * first list is a list of transactions that were loaded
      * second list is a list of transactions that were duplicates
      * third list is a list of transactions that were not loaded
    Example:
    """

    def __init__(self, account, transactions):
        self.account = account
        self.queued_transactions = transactions
        self.loaded_transactions = []
        self.duplicate_transactions = []
        self.failed_transactions = []

    def load(self):
        for candidate_transaction in self.queued_transactions:
            self._process(candidate_transaction)

        return [
            self.loaded_transactions,
            self.duplicate_transactions,
            self.failed_transactions,
        ]

    def _process(self, transaction):
        self.staged_transaction = Transaction(
            account_id=self.account.id,
            symbol=transaction['symbol']
        )
        try:
            self._check()
        else:
            self._load()
            self.loaded_transactions.append(self.staged_transaction)

    def _check(self):
        self.staged_transaction.full_clean()

    def _load(self):
        self.staged_transaction.save()

