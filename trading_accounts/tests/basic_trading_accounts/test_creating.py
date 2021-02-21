"""Define tests for creating"""
from django.test import TestCase, tag
from rest_framework import status
from users.models import User
from ..helpers.api_service import ApiService
from ..helpers.payload_factory import PayloadFactory
from ...models import TradingAccount


class CreatingTests(TestCase):
    """Test Creating"""

    def setUp(self):
        self.api_service = ApiService()

    @tag('integration')
    def test_creating_with_user(self):
        """test creating with associated user"""

        initial_number_of_accounts = TradingAccount.objects.count()

        username = 'arbitrary user'
        user = User(username=username)
        user.save()
        
        account_name = 'arbitrary account name'
        payload_factory = PayloadFactory({
            'name': account_name,
            'owner_id': user.id,
        })
        response = self.api_service.post(
            payload_factory.create_payload()
        )
        account_id = response.json()['data']['id']

        number_of_accounts_created = 1
        expected_number_of_accounts = (
            initial_number_of_accounts + number_of_accounts_created
        )
        self.assertEqual(
            TradingAccount.objects.count(),
            expected_number_of_accounts
        )

        account_in_database = TradingAccount.objects.get(pk=account_id)
        self.assertEqual(
            account_in_database.name,
            account_name
        )
        self.assertEqual(
            account_in_database.owner.username,
            username
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expected_key = 'data'
        self.assertTrue(expected_key in response.json())

    @tag('integration')
    def test_creating_without_user(self):
        """test creating"""

        initial_number_of_accounts = TradingAccount.objects.count()
        payload_factory = PayloadFactory()
        response = self.api_service.post(payload_factory.create_payload_without_owner())

        number_of_accounts_created = 0
        expected_number_of_accounts = (
            initial_number_of_accounts + number_of_accounts_created
        )
        self.assertEqual(
            TradingAccount.objects.count(),
            expected_number_of_accounts
        )

        expected_status_code = status.HTTP_400_BAD_REQUEST
        self.assertEqual(
            response.status_code,
            expected_status_code
        )

