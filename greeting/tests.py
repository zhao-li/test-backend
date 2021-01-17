"""Define tests for entire module"""
import json
from django.test import Client, TestCase, tag
from rest_framework import status
from .models import Greeting

TYPE = 'greetings'


class GreetingTests(TestCase):
    """Test Greeter API"""

    def setUp(self):
        self.client = Client()

    @tag('integration')
    def test_reading(self):
        """test reading"""
        response = self.client.get('/greetings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @tag('integration')
    def test_for_json_api_compliance(self):
        """test response complies with json api spec"""
        response = self.client.get('/greetings/')

        expected_key = 'data'
        self.assertTrue(expected_key in response.json())

    @tag('integration')
    def test_creating(self):
        """test creating"""

        message = 'greetings'
        json_data = {
            'data': {
                'type': TYPE,
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

    @tag('integration')
    def test_creating_and_reading(self):
        """test creating and reading"""

        message = 'A Greeting'
        json_data = {
            'data': {
                'type': TYPE,
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
