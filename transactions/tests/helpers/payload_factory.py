"""Define Payload Factory for tests"""
import json
from django.core.exceptions import ValidationError
from django.test import Client
from django.utils.translation import gettext as _


class PayloadFactory(Client):
    """A factory for generating payloads"""

    DEFAULT_SYMBOL = 'TGT'
    TRANSACTION_TYPE = 'transaction'
    TRADING_ACCOUNT_TYPE = 'tradingAccount'

    def __init__(self, overrides={}):
        self.overrides = overrides

    def create_payload(self):
        return {
            'data': {
                'type': self.TRANSACTION_TYPE,
                'attributes': {
                    'symbol': self._get_symbol(),
                },
                'relationships': {
                    'account': {
                        'data': {
                            'type': self.TRADING_ACCOUNT_TYPE,
                            'id': self._get_account_id(),
                        }
                    }
                }
            }
        }

    def create_payload_without_account(self):
        return {
            'data': {
                'type': self.TRANSACTION_TYPE,
                'attributes': {
                },
            }
        }

    def update_payload(self):
        return {
            'data': {
                'type': 'transaction',
                'id': self._get_id(),
                'attributes': {
                    'symbol': self._get_symbol(),
                }
            }
        }

    def file_upload_payload(self, file):
        return {
            'account_id': self._get_account_id(),
            'file': file,
        }

    def _get_id(self):
        if 'id' in self.overrides:
            return self.overrides['id']
        else:
            raise ValidationError(_('Missing account id'))

    def _get_symbol(self):
        if 'symbol' in self.overrides:
            return self.overrides['symbol']
        else:
            return self.DEFAULT_SYMBOL

    def _get_account_id(self):
        if 'account_id' in self.overrides:
            return self.overrides['account_id']
        else:
            raise ValidationError(_('Missing account id'))

