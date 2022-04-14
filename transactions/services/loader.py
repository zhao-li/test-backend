"""Define Loader for Transactions"""
from django.core.exceptions import ValidationError
from transactions.models import Transaction


class Loader():
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
        self.valid_transactions = []
        self.duplicate_transactions = []
        self.dirty_transactions = []

    def load(self):
        for candidate_transaction in self.queued_transactions:
            self._process(candidate_transaction)

        return [
            self.valid_transactions,
            self.duplicate_transactions,
            self.dirty_transactions,
        ]

    def _process(self, transaction):
        self.staged_transaction = Transaction(
            account=self.account,
            symbol=transaction.get('symbol'),
        )
        try:
            self._check()
        except ValidationError as error:
            all_errors = ''.join(error.message_dict.get('__all__', ''))
            if 'already exists' in all_errors:
                self.duplicate_transactions.append(self.staged_transaction)
            else:
                self.dirty_transactions.append(self.staged_transaction)
        else:
            self._load()
            self.valid_transactions.append(self.staged_transaction)

    def _check(self):
        self.staged_transaction.full_clean()

    def _load(self):
        self.staged_transaction.save()

