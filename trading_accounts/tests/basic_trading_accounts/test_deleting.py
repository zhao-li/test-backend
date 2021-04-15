"""Define tests for deleting"""
from django.test import TestCase, tag
from rest_framework import status
from users.models import User
from ..helpers.api_service import ApiService
from ..helpers.payload_factory import PayloadFactory
from ...models import TradingAccount


class DeletingTests(TestCase):
    """Test Deleting"""

    def setUp(self):
        self.api_service = ApiService()
        username = 'arbitrary user'
        user = User(username=username)
        user.save()
        payload_factory = PayloadFactory({
            'owner_id': user.id,
        })
        response = self.api_service.post(payload_factory.create_payload())
        self.account_id = response.json()['data']['id']

    @tag('integration')
    def test_deleting(self):
        """test deleting"""

        initial_number_of_accounts = TradingAccount.objects.count()
        response = self.api_service.delete(self.account_id)

        number_of_accounts_deleted = 1
        expected_number_of_accounts = (
            initial_number_of_accounts - number_of_accounts_deleted
        )
        self.assertEqual(
            TradingAccount.objects.count(),
            expected_number_of_accounts
        )
        with self.assertRaises(TradingAccount.DoesNotExist):
            TradingAccount.objects.get(pk=self.account_id)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

