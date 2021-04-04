"""Define Parser for Transacations"""
import csv


class TransactionsParser():
    """
    A parser for reading in transactdions
    Input: List of transactions as strings for each row of transaction data
    Example:
        ['"","Name","Symbol","Exchange","Open Date","Type","Amount","Open Price","Close Date","Close Price","Gain%","Net P/L"', '"","Fastly","FSLY.K","NYSE","01/07/2021","BUY","100.00000000","86.41","01/08/2021","86.41","0.00%","$0.00"', '"","Overstockcom","OSTK.O","NASDAQ","01/05/2021","BUY","100.00000000","53.42","01/07/2021","57.16","7.00%","$374.00"']
    Output: List of transactions as dicts
    """

    def __init__(self, raw_data_string):
        self.raw_data_string = raw_data_string

    def parse(self):
        self._read_data()
        self._transform_fieldnames()
        return list(self.reader)

    def _read_data(self):
        self.reader = csv.DictReader(self.raw_data_string)

    def _transform_fieldnames(self):
        self.reader.fieldnames = [fieldname.lower() for fieldname in self.reader.fieldnames]

