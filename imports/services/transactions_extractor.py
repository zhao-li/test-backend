"""Define Extractor for Transacations"""


class TransactionsExtractor():
    """
    An extractor for transactdions in an Investing.com portfolio export
    Input: CSV String
    Output: List of transaction strings for each row of transaction data
    """

    START_DELIMITER = '''"Closed Positions"'''
    STOP_DELIMITER = ""

    def __init__(self, raw_data_string):
        self.raw_data_string = raw_data_string
        self.transaction_lines = []
        self.started_flag = False
        self.ended_flag = False

    def extract(self):
        for line in self.raw_data_string.split("\n"):
            if self._transaction_section_had_started():
                if self._transaction_section_should_be_stopping(line):
                    self._stop_on_this_line()
                else:
                    self._save(line)
            else:
                if self._transaction_section_should_be_starting(line):
                    self._start_saving_next_lines_as_transactions()
            if self._this_is_last_line():
                break 
        return self.transaction_lines

    def _transaction_section_had_started(self):
        return self.started_flag == True

    def _transaction_section_should_be_starting(self, line):
        return line == self.START_DELIMITER

    def _start_saving_next_lines_as_transactions(self):
        self.started_flag = True

    def _this_is_last_line(self):
        return self.ended_flag == True

    def _transaction_section_should_be_stopping(self, line):
        return line == self.STOP_DELIMITER

    def _stop_on_this_line(self):
        self.ended_flag = True

    def _save(self, line):
        self.transaction_lines.append(line)

