"""Test Greeting Module"""

import json

from rest_framework import status
from django.test import Client, TestCase

from .models import Greeting


class GreetingTests(TestCase):
    """Test Greeter API"""

    def setUp(self):
        self.client = Client()

    def test_fetching_greeters(self):
        """test getting a list of greeters"""
        response = self.client.get('/greetings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_for_json_api_compliance(self):
        """test response complies with json api spec"""
        response = self.client.get('/greetings/')

        expected_key = 'data'
        self.assertTrue(expected_key in response.json())

    def test_creating_greeter(self):
        """test creating a greeting"""

        message = 'greetings'
        json_data = {
            'data': {
                'type': 'greeting',
                'attributes': {
                    'message': message
                }
            }
        }

        response = self.client.post(
            '/greetings/',
            json.dumps(json_data),
            content_type='application/vnd.api+json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expected_message = message
        self.assertEqual(
            Greeting.objects.first().message,
            expected_message
        )

    def test_creating_and_getting_greeting(self):
        """test creating a greeting"""

        message = 'greetings'
        json_data = {
            'data': {
                'type': 'greeting',
                'attributes': {
                    'message': message
                }
            }
        }

        response = self.client.post(
            '/greetings/',
            json.dumps(json_data),
            content_type='application/vnd.api+json'
        )

        expected_message = message
        self.assertEqual(Greeting.objects.first().message, expected_message)

        response = self.client.get('/greetings/')
        first_greeter = 0
        self.assertEqual(
            response.json()['data'][first_greeter]['attributes']['message'],
            expected_message
        )
