"""Define tests for updating"""
from django.test import TestCase, tag
from rest_framework import status
from trading_accounts.models import TradingAccount
from users.models import User
from ..helpers.api_service import ApiService
from ..helpers.payload_factory import PayloadFactory
from ...models import Transaction


class UpdatingTests(TestCase):
    """Test Updating"""

    def setUp(self):
        self.api_service = ApiService()
        username = 'arbitrary user'
        user = User(username=username)
        user.save()
        account_name = 'account name'
        self.account = TradingAccount(
          owner_id=user.id,
          name=account_name,
        )
        self.account.save()

        original_symbol = 'arbitrary symbol'
        payload_factory = PayloadFactory({
            'account_id': self.account.id,
            'symbol': original_symbol,
        })
        response = self.api_service.post(
            payload_factory.create_payload()
        )
        self.transaction_id = response.json()['data']['id']

    @tag('integration')
    def test_updating(self):
        """test updating"""

        updated_symbol = 'Updated Symbol'
        payload_factory = PayloadFactory({
            'id': self.account.id,
            'symbol': updated_symbol,
        })
        response = self.api_service.patch(
            self.transaction_id,
            payload_factory.update_payload(),
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_key = 'data'
        self.assertTrue(expected_key in response.json())

        expected_symbol = updated_symbol
        self.assertEqual(
            Transaction.objects.get(pk=self.transaction_id).symbol,
            expected_symbol
        )

