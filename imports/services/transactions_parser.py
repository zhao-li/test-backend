"""Define Parser for Transacations"""
import csv


class TransactionsParser():
    """
    A parser for reading in transactdions
    Input: CSV String
    Output: List of transactions
    """

    def __init__(self, raw_data_string):
        self.raw_data_string = raw_data_string

    def parse(self):
        self.reader = csv.reader(self.raw_data_string)
        for row in self.reader:
            print("===")
            print(row)
        return self.raw_data_string

