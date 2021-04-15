"""Define tests for updating"""
from django.test import TestCase, tag
from rest_framework import status
from users.models import User
from ..helpers.api_service import ApiService
from ..helpers.payload_factory import PayloadFactory
from ...models import TradingAccount


class UpdatingTests(TestCase):
    """Test Updating"""

    def setUp(self):
        self.api_service = ApiService()
        username = 'arbitrary user'
        user = User(username=username)
        user.save()
        original_account_name = 'original account name'
        payload_factory = PayloadFactory({
            'name': original_account_name,
            'owner_id': user.id,
        })
        response = self.api_service.post(
            payload_factory.create_payload()
        )
        self.account_id = response.json()['data']['id']

    @tag('integration')
    def test_updating(self):
        """test updating"""

        updated_name = 'An Updated Trading Account Name'
        payload_factory = PayloadFactory({
            'id': self.account_id,
            'name': updated_name,
        })
        response = self.api_service.patch(
            self.account_id,
            payload_factory.update_payload(),
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_key = 'data'
        self.assertTrue(expected_key in response.json())

        expected_name = updated_name
        self.assertEqual(
            TradingAccount.objects.get(pk=self.account_id).name,
            expected_name
        )

