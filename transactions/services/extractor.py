"""Define Extractor for Transacations"""


class Extractor():
    """
    An extractor for transactdions in an Investing.com portfolio export
    Input: String of entire CSV file
    Example: 
        "Open Positions"
        "","Name","Symbol","Exchange","Open Date","Type","Amount","Open Price",
        "Current Price","Extended Hours","Extended Hours (%)","Prev.",
        "Market Value","Commission","Net P/L%","Weight","Daily P/L","Daily P/L%","Net P/L","Next Earnings Date"
        "","Unity Software","U","NYSE","01/08/2021","BUY","35.00000000","147.22","146.20","146.43","0.16%","138.57","$5,117.00","$0.00","-0.69%","3.09%","$267.05","5.51%","-$35.70","May 13, 2021"
        "","Fastly","FSLY.K","NYSE","01/07/2021","BUY","100.00000000","86.41","88.22","88.25","0.03%","86.91","$8,822.00","$0.00","2.09%","5.33%","$131.00","1.51%","$181.00","May 12, 2021"

        "Closed Positions"
        "","Name","Symbol","Exchange","Open Date","Type","Amount","Open Price","Close Date","Close Price","Gain%","Net P/L"
        "","Fastly","FSLY.K","NYSE","01/07/2021","BUY","100.00000000","86.41","01/08/2021","86.41","0.00%","$0.00"
        "","Overstockcom","OSTK.O","NASDAQ","01/05/2021","BUY","100.00000000","53.42","01/07/2021","57.16","7.00%","$374.00"

        "Closed P/L","$65,710.05"
    Output: List of transactions as strings for each row of transaction data
    Example:
        ['"","Name","Symbol","Exchange","Open Date","Type","Amount","Open Price","Close Date","Close Price","Gain%","Net P/L"', '"","Fastly","FSLY.K","NYSE","01/07/2021","BUY","100.00000000","86.41","01/08/2021","86.41","0.00%","$0.00"', '"","Overstockcom","OSTK.O","NASDAQ","01/05/2021","BUY","100.00000000","53.42","01/07/2021","57.16","7.00%","$374.00"']
    """  # nopep8

    START_DELIMITER = '''"Closed Positions"'''
    STOP_DELIMITER = ""

    def __init__(self, raw_data_string):
        self.raw_data_string = raw_data_string
        self.transaction_lines = []
        self.start_flag = False
        self.stop_flag = False

    def extract(self):
        for line in self.raw_data_string.split("\n"):
            self._process(line)
            if self._this_is_last_line():
                break
        return self.transaction_lines

    def _process(self, line):
        if self._current_line_is_the_beginning_of_transactions_section(line):
            self._start_saving_next_lines_as_transactions()
        elif self._current_line_is_the_ending_of_transactions_section(line):
            self._stop_on_this_line()
        elif self._current_line_is_a_transaction():
            self._save(line)
        elif self._current_line_is_not_useful():
            pass  # do nothing

    def _this_is_last_line(self):
        return self.start_flag is True and self.stop_flag is True

    def _current_line_is_the_beginning_of_transactions_section(self, line):
        return line == self.START_DELIMITER

    def _start_saving_next_lines_as_transactions(self):
        self.start_flag = True

    def _current_line_is_the_ending_of_transactions_section(self, line):
        return line is self.STOP_DELIMITER and self.start_flag is True

    def _stop_on_this_line(self):
        self.stop_flag = True

    def _current_line_is_a_transaction(self):
        return self.start_flag is True and self.stop_flag is False

    def _save(self, line):
        self.transaction_lines.append(line)

    def _current_line_is_not_useful(self):
        return self.start_flag is False

