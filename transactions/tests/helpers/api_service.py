"""Define API Service for tests"""
import json
from django.conf import settings
from django.test import Client


class ApiService(Client):
    """A service for testing API"""

    PATH = '/transactions/'
    CONTENT_TYPE = settings.JSON_API_CONTENT_TYPE

    def __init__(self):
        self.client = Client()

    def get_all(self):
        return self.client.get(self.PATH)

    def get_one(self, id):
        return self.client.get(self.PATH + str(id) + '/')

    def post(self, payload):
        return self.client.post(
            self.PATH,
            json.dumps(payload),
            content_type=self.CONTENT_TYPE,
        )

    def patch(self, id, payload):
        return self.client.patch(
            self.PATH + str(id) + '/',
            data=json.dumps(payload),
            content_type=self.CONTENT_TYPE,
        )

    def delete(self, id):
        return self.client.delete(
            self.PATH + str(id) + '/',
            content_type=self.CONTENT_TYPE,
        )

    def batch_upload(self, payload):
        return self.client.post(
            self.PATH + 'batch_upload/',
            payload,
        )

