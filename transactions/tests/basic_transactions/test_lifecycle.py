"""Define tests for entire lifecycle"""
from django.test import TestCase, tag
from rest_framework import status
from trading_accounts.models import TradingAccount
from users.models import User
from ..helpers.api_service import ApiService
from ..helpers.payload_factory import PayloadFactory


class LIfeCycleTests(TestCase):
    """Test Life Cycle"""

    def setUp(self):
        self.api_service = ApiService()

        username = 'arbitrary user'
        user = User(username=username)
        user.save()

        self.account_name = 'arbitrary account name'
        self.account = TradingAccount(
            name=self.account_name,
            owner=user,
        )
        self.account.save()

    @tag('integration')
    def test_life_cycle(self):
        """test life cycle"""

        original_symbol = 'original symbol'
        payload_factory = PayloadFactory({
            'account_id': self.account.id,
            'symbol': original_symbol,
        })
        response = self.api_service.post(
            payload_factory.create_payload()
        )
        transaction_id = response.json()['data']['id']

        response = self.api_service.get_one(transaction_id)
        self.assertEqual(
            response.json()['data']['attributes']['symbol'],
            original_symbol
        )

        updated_payload = response.json()
        updated_symbol = 'Updated Symbol'
        updated_payload['data']['attributes']['symbol'] = updated_symbol
        response = self.api_service.patch(transaction_id, updated_payload)

        response = self.api_service.get_one(transaction_id)
        expected_symbol = updated_symbol
        self.assertEqual(
            response.json()['data']['attributes']['symbol'],
            expected_symbol
        )

        response = self.api_service.delete(transaction_id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

