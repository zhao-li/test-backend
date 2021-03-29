"""Define Extractor for Transacations"""
import csv


class TransactionsExtractor():
    """
    An extractor for transactdions in an Investing.com portfolio export
    Input: CSV String
    Output: List of transaction strings for each row of transaction data
    """

    def __init__(self, raw_data_string):
        self.raw_data_string = raw_data_string

    def extract(self):
        self.reader = csv.reader(self.raw_data_string)
        for row in self.reader:
            print("===")
            print(row)
        return self.raw_data_string

