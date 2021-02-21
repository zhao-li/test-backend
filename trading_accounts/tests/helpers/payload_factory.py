"""Define Payload Factory for tests"""
import json
from django.core.exceptions import ValidationError
from django.test import Client
from django.utils.translation import gettext as _


class PayloadFactory(Client):
    """A factory for generating payloads"""

    DEFAULT_NAME = 'An Arbitrary Name'

    def __init__(self, overrides={}):
        self.overrides = overrides

    def create_payload(self):
        return {
            'data': {
                'type': 'tradingAccounts',
                'attributes': {
                    'name': self._get_name(),
                },
                'relationships': {
                    'owner': {
                        'data': {
                            'type': 'users',
                            'id': self._get_owner_id(),
                        }
                    }
                }
            }
        }

    def create_payload_without_owner(self):
        return {
            'data': {
                'type': 'tradingAccounts',
                'attributes': {
                    'name': self._get_name(),
                },
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
            raise ValidationError(_('Missing account id'))

    def _get_name(self):
        if 'name' in self.overrides:
            return self.overrides['name']
        else:
            return self.DEFAULT_NAME

    def _get_owner_id(self):
        if 'owner_id' in self.overrides:
            return self.overrides['owner_id']
        else:
            raise ValidationError(_('Missing owner id'))

