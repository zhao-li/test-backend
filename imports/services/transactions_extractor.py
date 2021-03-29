"""Define Extractor for Transacations"""


class TransactionsExtractor():
    """
    An extractor for transactdions in an Investing.com portfolio export
    Input: String of entire CSV file
    Output: List of transactions as strings for each row of transaction data
    """

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
            pass # do nothing

    def _this_is_last_line(self):
        return self.start_flag == True and self.stop_flag == True

    def _current_line_is_the_beginning_of_transactions_section(self, line):
        return line == self.START_DELIMITER

    def _start_saving_next_lines_as_transactions(self):
        self.start_flag = True

    def _current_line_is_the_ending_of_transactions_section(self, line):
        return line == self.STOP_DELIMITER and self.start_flag == True

    def _stop_on_this_line(self):
        self.stop_flag = True

    def _current_line_is_a_transaction(self):
        return self.start_flag == True and self.stop_flag == False

    def _save(self, line):
        self.transaction_lines.append(line)

    def _current_line_is_not_useful(self):
        return self.start_flag == False

