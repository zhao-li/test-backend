"""Define API Service for tests"""
import json
from django.test import Client


class ApiService(Client):
    """A service for testing API"""

    PATH = '/greetings/'
    CONTENT_TYPE = 'application/vnd.api+json'

    def __init__(self):
        self.client = Client()

    def post(self, payload):
        return self.client.post(
            self.PATH,
            json.dumps(payload),
            content_type=self.CONTENT_TYPE,
        )

