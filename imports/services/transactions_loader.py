"""Define Loader for Transactions"""


class TransactionsLoader():
    """
    A loader for transactions
    Note: load means saving to storage
    Input: 
    Example: 
    Output: A list of 2 lists
      * first list is a list of successfully loaded transactions
      * second list is a list of duplicate transactions that were not loaded
    Example:
    """

    def __init__(self, transactions):
        self.transactions = transactions

    def load(self):
        return [True, False]

