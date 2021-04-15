"""Define API Service for tests"""
import json
from django.test import Client


class ApiService(Client):
    """A service for testing API"""

    PATH = '/imports/'

    def __init__(self):
        self.client = Client()

    def post_transactions(self, account_id, csv_file):
        return self.client.post(
            self.PATH + 'transactions/',
            {
                'account_id': account_id,
                'attachment': csv_file,
            },
        )

