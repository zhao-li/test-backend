"""Define Payload Factory for tests"""
import json
from django.test import Client


class PayloadFactory(Client):
    """A factory for generating payloads"""

    DEFAULT_ID = '1'
    DEFAULT_NAME = 'An Arbitrary Name'

    def __init__(self, overrides={}):
        self.overrides = overrides

    def create_payload(self):
        return {
            'data': {
                'type': 'tradingAccounts',
                'attributes': {
                    'name': self._get_name()
                }
            }
        }

    def update_payload(self):
        return {
            'data': {
                'type': 'tradingAccounts',
                'id': self._get_id(),
                'attributes': {
                    'name': self._get_name()
                }
            }
        }

    def _get_id(self):
        if 'id' in self.overrides:
            return self.overrides['id']
        else:
            return self.DEFAULT_ID

    def _get_name(self):
        if 'name' in self.overrides:
            return self.overrides['name']
        else:
            return self.DEFAULT_NAME

