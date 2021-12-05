"""Define Payload Factory for tests"""
import json
from django.test import Client


class PayloadFactory(Client):
    """A factory for generating payloads"""

    TYPE = 'greeting'
    DEFAULT_ID = '1'
    DEFAULT_MESSAGE = 'An Arbitrary Message'

    def __init__(self, overrides={}):
        self.overrides = overrides

    def create_payload(self):
        return {
            'data': {
                'type': self._get_type(),
                'attributes': {
                    'message': self._get_message()
                }
            }
        }

    def update_payload(self):
        return {
            'data': {
                'type': self._get_type(),
                'id': self._get_id(),
                'attributes': {
                    'message': self._get_message()
                }
            }
        }

    def _get_type(self):
        return self.TYPE

    def _get_id(self):
        if 'id' in self.overrides:
            return self.overrides['id']
        else:
            return self.DEFAULT_ID

    def _get_message(self):
        if 'message' in self.overrides:
            return self.overrides['message']
        else:
            return self.DEFAULT_MESSAGE

